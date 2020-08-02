# Image Preprocessing
- Hyojung Chang
- Jonggeun Park
- Minjoo Lee

## roi_from_luna16.py
- Extract ```ROI``` from CT images(mhd) provided by LUNA16 
(```ROI```: The area where the nodule is located)
- ```ROI``` is saved as .png
- Edit **save_path/src_root/dst_root** before running

## roi_from_covid(Larxel)
### nii2png.py
- Convert .nii to .png
### roi_from_covid(Larxel).py
- Extract ```ROI``` from CT images provided by https://www.kaggle.com/andrewmvd/covid19-ct-scans/data
(```ROI```: The lung area of a person suffering from a corona.)
- ```ROI``` is saved as .png
- Edit **save_path/src_root** before running


## roi_from_tcia
- Extract ```ROI``` from CT images(dicom) provided by [TCIA](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70224216)
(```ROI```: The area where the nodule is located)
- ```ROI``` is saved as .png
