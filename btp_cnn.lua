require 'paths'
require 'nn'
require 'optim'

dataset = torch.load('dataset.t7')
trainset = {}
testset = {}

trainset['data'] = dataset['images'][{{1,500},{},{},{}}]
trainset['labels'] = dataset['labels'][{{1,500}}]

testset['data'] = dataset['images'][{{501,576},{},{},{}}]
testset['labels'] = dataset['labels'][{{501,576}}]

setmetatable(trainset, 
    {__index = function(t, i) 
                    return {t.data[i], t.labels[i]} 
                end}
);

trainset.data = trainset.data:double()

function trainset:size() 
    return self.data:size(1) 
end
	
mean = trainset.data:mean()
print ('Mean = ' .. mean)
trainset.data = trainset.data:add(-mean)
stdv = trainset.data:std()
print('Stdv = ' .. stdv)
trainset.data = trainset.data:div(stdv)

testset.data = testset.data:double()
testset.data = testset.data:add(-mean)
testset.data = testset.data:div(stdv)

net = nn.Sequential()
net:add(nn.SpatialConvolution(3, 6, 5, 5)) 
net:add(nn.ReLU())                       
net:add(nn.SpatialMaxPooling(2,2,2,2))     
net:add(nn.SpatialConvolution(6, 8,5,5))
net:add(nn.ReLU())                       
net:add(nn.SpatialMaxPooling(2,2,2,2))
net:add(nn.View(8*61*61))                 
net:add(nn.Linear(8*61*61,20))          
net:add(nn.ReLU())                       
net:add(nn.Linear(20, 8))
net:add(nn.ReLU())                       
net:add(nn.Linear(8,2))               
net:add(nn.LogSoftMax())

learning_rate = 0.001
criterion = nn.ClassNLLCriterion()
batch_size = 10
epoch = 10

function sgd(x, dx, lr)
  x:add(-lr, dx)
end

function accuracy(testset,net)
	correct = 0
	for i=1,76 do
	    local groundtruth = testset.labels[i]+1
	    local prediction = net:forward(testset.data[i])
	    local confidences, indices = torch.sort(prediction, true)  -- true means sort in descending order
	    if groundtruth == indices[1] then
	        correct = correct + 1
	    end
	end
	print(correct, 100*correct/76 .. ' % ')
end

-- function class_performances(testset,net)
--     class_performance = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
--     total_classes = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
--     for i=1,10000 do
--         local groundtruth = testset.labels[i]
--         total_classes[testset.labels[i]] = total_classes[testset.labels[i]] + 1 
--         local prediction = net:forward(testset.data[i])
--         local confidences, indices = torch.sort(prediction, true)  -- true means sort in descending order
--         if groundtruth == indices[1] then
--             class_performance[groundtruth] = class_performance[groundtruth] + 1
--         end
--     end
--     for i=1,10 do
--         print(i,100*class_performance[i]/total_classes[i])
--     end
-- end

function train(trainset)
    params,grad_params = net:getParameters()
    for l=1,epoch do  
        -- time_start = sys.clock()
        for t = 1,trainset:size()/batch_size do
        	currentError = 0
        	grad_params:zero()
        	local input = torch.zeros(batch_size,3,256,256)
        	local target = torch.zeros(batch_size)
        	for s = 1,batch_size do
    	        local example = trainset[(t-1)*batch_size+s];
    	        input[s] = example[1];
    	        target[s] = example[2];
    	    end
            a = net:forward(input)
            -- print(a)
            -- target =2 
            error = criterion:forward(a, target+1);
            print(t,error)
            currentError = currentError + error
            net:backward(input, criterion:backward(net.output, target+1));
            sgd(params,grad_params,learning_rate)
            xlua.progress(t,trainset:size()/batch_size)
        end
        -- time_end = sys.clock()
        accuracy(testset,net)
        -- class_performances(testset,net)
    end
    -- return(time_end-time_start)
end

-- logger = optim.Logger('./benchmark.log')
-- logger:setNames{'Batch Size', 'Time Taken in s'}

-- batch_size = torch.Tensor({1,2,5,10,20,50,100,200,500,1000})
-- epoch = 1
-- time_taken = torch.Tensor(10)


-- for i=1,batch_size:size()[1] do 
--     time_taken[i] = train(trainset,batch_size[i],epoch,create_net(),learning_rate)
--     logger:add{batch_size[i],time_taken[i]}
-- end

-- logger:style{'+-', '+-'}

train(trainset)



torch.save('mnist_cnn_trained.t7',net)             

















