#docker exec -it cvat bash -ic 'python3 ~/cvat/apps/auto_annotation/run_model.py --model-name "Mask RCNN Object Detector" --task-id 21'
docker exec -it cvat bash -ic "python3 ~/utils/auto_annotation/run_model.py --model-name mask_rcnn_inception_resnet_v2_atrous_coco --task-id 1"

#python ../utils/auto_annotation/run_model.py --model-name "Mask RCNN Object Detector" --task-id 21
