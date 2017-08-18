require 'image'
require 'paths'

i=0
j=0

for file in paths.files('Bad') do
	if file:find('.png') then
		i=i+1
	end
end

for file in paths.files('Good') do
	if file:find('.png') then
		j=j+1
	end
end

total = i+j

t = {}


images = torch.zeros(total,3,256,256)
labels = torch.zeros(total)


i=1
for file in paths.files('Bad') do
	if file:find('.png') then
		imgpath = paths.concat('Bad',file)
		img = image.load(imgpath)
		images[i] = img[{{1,3},{},{}}]
		labels[i] = 0
		i=i+1
	end
end

for file in paths.files('Good') do
	if file:find('.png') then
		imgpath = paths.concat('Good',file)
		img = image.load(imgpath)
		images[i] = img[{{1,3},{},{}}]
		labels[i] = 1
		i=i+1
	end
end

perm = torch.randperm(total)
temp_imgs = torch.zeros(total,3,256,256)
temp_labels = torch.zeros(total)

for i=1,total do
	temp_imgs[i] = images[perm[i]]
	temp_labels[i] = labels[perm[i]]
end


t['images'] = temp_imgs
t['labels'] = temp_labels

torch.save('dataset.t7',t)

