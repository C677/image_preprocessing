# Image Preprocessing
- Hyojung Chang
- Jonggeun Park
- Minjoo Lee

## roi_from_luna16.py
- Extract ```ROI``` from CT images(mhd) provided by LUNA16 
(```ROI```: The area where the nodule is located)
- ```ROI``` is saved as ```nodule_annotations.csv```
- ```nodule_annotations.csv``` is composed of [filename, minX, maxX, minY, maxY, classname]
- Edit **save_path/src_root/dst_root** before running

## roi_from_covid(Larxel)
### nii2png.py
- Convert .nii to .png
### roi_from_covid(Larxel).py
- Extract ```ROI``` from CT images provided by https://www.kaggle.com/andrewmvd/covid19-ct-scans/data
(```ROI```: The lung area of a person suffering from a corona)
- ```ROI``` is saved as ```covid(Larxel)_annotations.csv```
- ```covid(Larxel)_annotations.csv``` is composed of [filename, minX, maxX, minY, maxY, classname]
- Edit **save_path/src_root** before running


## roi_from_tcia
- Extract ```ROI``` from CT images(dicom) provided by [TCIA](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70224216)
(```ROI```: The area where the nodule is located)
- ```ROI``` is saved as .png

## roi_from_covid(LuisBlanche)
### lung_model.hdf5
- model of tracking lung segmentation from CT image
- reference : https://github.com/kairess/CT_lung_segmentation
- 정확도가 높지 않음. 참고를 위해 작성하였을 뿐 사용은 추천하지 않음.
### roi_from_covid(LuisBlanche).py
- Extract ```ROI``` from CT images provided by https://www.kaggle.com/luisblanche/covidct
(```ROI```: The lung area of a person suffering from a corona)
- ```ROI``` is saved as .png
- Edit **save_path/src_root** before running

## roi_from_covid(MedSeg)
### roi_from_covid(MedSeg).py
- Extract ```ROI``` from CT images provided by MedSeg
(```ROI```: The lung area of a person suffering from a corona)
- ```ROI``` is saved as ```covid(MedSeg)_annotations.csv```
- ```covid(MedSeg)_annotations.csv``` is composed of [filename, minX, maxX, minY, maxY, classname]
- Edit **save_path/src_root** before running
