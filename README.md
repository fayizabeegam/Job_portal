Job Portal
===
Abstract:xxx
## Papar Information
- Title:  `paper name`
- Authors:  `A`,`B`,`C`
- Preprint: [https://arxiv.org/abs/xx]()
- Full-preprint: [paper position]()
- Video: [video position]()

## Install & Dependence
- python
- pytorch
- numpy

## Dataset Preparation
| Dataset | Download |
| ---     | ---   |
| dataset-A | [download]() |
| dataset-B | [download]() |
| dataset-C | [download]() |

## Use
- for train
  ```
  python train.py
  ```
- for test
  ```
  python test.py
  ```
## Pretrained model
| Model | Download |
| ---     | ---   |
| Model-1 | [download]() |
| Model-2 | [download]() |
| Model-3 | [download]() |


## Directory Hierarchy
```
|—— accounts
|    |—— admin.py
|    |—— apps.py
|    |—— forms.py
|    |—— managers.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-312.pyc
|            |—— 0002_alter_user_profile_pic.cpython-312.pyc
|            |—— 0002_user_is_admin_registered.cpython-312.pyc
|            |—— 0003_remove_user_profile_pic.cpython-312.pyc
|            |—— __init__.cpython-312.pyc
|    |—— models.py
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|    |—— __pycache__
|        |—— admin.cpython-312.pyc
|        |—— apps.cpython-312.pyc
|        |—— forms.cpython-312.pyc
|        |—— managers.cpython-312.pyc
|        |—— models.cpython-312.pyc
|        |—— urls.cpython-312.pyc
|        |—— views.cpython-312.pyc
|        |—— __init__.cpython-312.pyc
|—— adminapp
|    |—— admin.py
|    |—— apps.py
|    |—— forms.py
|    |—— migrations
|        |—— __init__.py
|        |—— __pycache__
|            |—— __init__.cpython-312.pyc
|    |—— models.py
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|    |—— __pycache__
|        |—— admin.cpython-312.pyc
|        |—— apps.cpython-312.pyc
|        |—— forms.cpython-312.pyc
|        |—— models.cpython-312.pyc
|        |—— urls.cpython-312.pyc
|        |—— views.cpython-312.pyc
|        |—— __init__.cpython-312.pyc
|—— db.sqlite3
|—— jobs
|    |—— admin.py
|    |—— apps.py
|    |—— decorators.py
|    |—— forms.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— 0002_jobcategory_alter_joblisting_category.py
|        |—— 0003_jobcategory_icon_image.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-312.pyc
|            |—— 0002_jobapplication_profile.cpython-312.pyc
|            |—— 0002_jobcategory_alter_joblisting_category.cpython-312.pyc
|            |—— 0002_joblisting_category.cpython-312.pyc
|            |—— 0002_jobseekerupdateprofile_is_active_and_more.cpython-312.pyc
|            |—— 0002_jobseekerupdateprofile_profile_pic_and_more.cpython-312.pyc
|            |—— 0002_profilepicture_and_more.cpython-312.pyc
|            |—— 0003_alter_jobseekerupdateprofile_profile_picture_and_more.cpython-312.pyc
|            |—— 0003_alter_profilepicture_picture.cpython-312.pyc
|            |—— 0003_jobcategory_icon_image.cpython-312.pyc
|            |—— 0003_remove_jobapplication_profile.cpython-312.pyc
|            |—— 0003_remove_joblisting_industry.cpython-312.pyc
|            |—— 0003_remove_jobseekerupdateprofile_profile_pic_and_more.cpython-312.pyc
|            |—— 0004_alter_jobapplication_job_seeker_and_more.cpython-312.pyc
|            |—— 0004_alter_joblisting_recruiter.cpython-312.pyc
|            |—— 0005_alter_joblisting_recruiter.cpython-312.pyc
|            |—— 0005_rename_job_seeker_jobapplication_name_and_more.cpython-312.pyc
|            |—— 0006_rename_position_jobapplication_job_listing_and_more.cpython-312.pyc
|            |—— 0007_alter_jobapplication_job_listing.cpython-312.pyc
|            |—— 0008_joblisting_status.cpython-312.pyc
|            |—— __init__.cpython-312.pyc
|    |—— models.py
|    |—— templatetags
|        |—— is_already_applied.py
|        |—— __pycache__
|            |—— custom_tag.cpython-312.pyc
|            |—— is_already_applied.cpython-312.pyc
|    |—— tests.py
|    |—— urls.py
|    |—— views
|        |—— home.py
|        |—— jobseeker.py
|        |—— recruiter.py
|        |—— __pycache__
|            |—— admindashboard.cpython-312.pyc
|            |—— home.cpython-312.pyc
|            |—— jobseeker.cpython-312.pyc
|            |—— recruiter.cpython-312.pyc
|    |—— __init__.py
|    |—— __pycache__
|        |—— admin.cpython-312.pyc
|        |—— apps.cpython-312.pyc
|        |—— decorators.cpython-312.pyc
|        |—— forms.cpython-312.pyc
|        |—— models.cpython-312.pyc
|        |—— urls.cpython-312.pyc
|        |—— __init__.cpython-312.pyc
|—— job_portal
|    |—— asgi.py
|    |—— settings.py
|    |—— urls.py
|    |—— wsgi.py
|    |—— __init__.py
|    |—— __pycache__
|        |—— settings.cpython-312.pyc
|        |—— urls.cpython-312.pyc
|        |—— wsgi.cpython-312.pyc
|        |—— __init__.cpython-312.pyc
|—— manage.py
|—— media
|    |—— applications
|        |—— Django_Main_Project_Details.pdf
|        |—— Django_Main_Project_Details_AKZP7uc.pdf
|        |—— Django_Main_Project_Details_Dtk3XJE.pdf
|        |—— Django_Main_Project_Details_OzWmT89.pdf
|        |—— Django_Main_Project_Details_UdG9yRY.pdf
|        |—— Django_Main_Project_Details_Wbmao9z.pdf
|        |—— Django_Main_Project_Details_WUhZcQ7.pdf
|        |—— Django_Main_Project_Details_yFnosLw.pdf
|    |—— category_images
|        |—— administration.png
|        |—— code.png
|        |—— data.png
|        |—— discussion.png
|        |—— healthcare.png
|        |—— hotel-cleaning.png
|        |—— legal-system.png
|        |—— profit.png
|        |—— reading-book.png
|        |—— salemarketing.png
|        |—— settings.png
|        |—— ux.png
|    |—— jobseeker_profile_pictures
|        |—— default.jpg
|        |—— pic1.jpg
|        |—— pic1_R7bqNK9.jpg
|        |—— pic2.jpg
|        |—— pic3.jpg
|        |—— pic3_3vdLqQR.jpg
|        |—— pic3_kc06GTr.jpg
|        |—— pic4.jpg
|    |—— profile_pictures
|        |—— default.jpg
|    |—— recruiter_profile_pictures
|        |—— default.jpg
|        |—— pic2.jpg
|        |—— pic2_8sDn5rb.jpg
|        |—— pic3.jpg
|        |—— pic3_kuFVoAM.jpg
|    |—— resumes
|        |—— Django_Main_Project_Details.pdf
|        |—— fayizacovee.pdf
|        |—— fayizacovee_6FkSsxT.pdf
|        |—— fayizacovee_eYKOVyO.pdf
|        |—— fayizacovee_FfQEr7f.pdf
|        |—— fayizacovee_lT3IrlU.pdf
|        |—— fayizacovee_sjwB0lr.pdf
|        |—— fayizacv.pdf
|        |—— Python_Challenge.pdf
|—— static
|    |—— css
|        |—— custom.css
|        |—— style.default.css
|    |—— img
|        |—— about.jpg
|        |—— administration.png
|        |—— avatar.png
|        |—— businessman-logo-with-bag-concept_11481-280.avif
|        |—— code.png
|        |—— data.png
|        |—— default_job.jpg
|        |—— discussion.png
|        |—— graphic-design.png
|        |—— healthcare.png
|        |—— hotel-cleaning.png
|        |—— icon.jpg
|        |—— jobs.jpg
|        |—— legal-system.png
|        |—— logo.png
|        |—— profit.png
|        |—— reading-book.png
|        |—— sale&marketing.png
|        |—— settings.png
|        |—— support-img.jpg
|        |—— ux.png
|    |—— js
|        |—— front.js
|        |—— script.js
|    |—— vendor
|        |—— bootstrap
|            |—— css
|                |—— bootstrap.min.css
|            |—— js
|                |—— bootstrap.min.js
|        |—— bootstrap-select
|            |—— css
|                |—— bootstrap-select.min.css
|            |—— js
|                |—— bootstrap-select.min.js
|        |—— font-awesome
|            |—— css
|                |—— font-awesome.min.css
|        |—— jquery
|            |—— jquery.min.js
|        |—— jquery.cookie
|            |—— jquery.cookie.js
|        |—— owl.carousel
|            |—— assets
|                |—— owl.carousel.css
|                |—— owl.theme.default.css
|                |—— owl.video.play.png
|            |—— owl.carousel.min.js
|        |—— popper.js
|            |—— umd
|                |—— popper.min.js
|—— templates
|    |—— accounts
|        |—— jobseeker
|            |—— register.html
|        |—— login.html
|        |—— recruiter
|            |—— register.html
|    |—— admin
|        |—— add_categories.html
|        |—— admin_home.html
|        |—— admin_recruiter_dashboard.html
|        |—— jobseeker_list.html
|        |—— jobseeker_profile_details.html
|        |—— recruiter_list.html
|        |—— recruiter_profile_details.html
|        |—— update_jobseeker_status.html
|    |—— base.html
|    |—— home.html
|    |—— jobs
|        |—— applied_jobs_list.html
|        |—— apply_job.html
|        |—— create.html
|        |—— details.html
|        |—— edit.html
|        |—— jobs.html
|        |—— jobseeker
|            |—— add_profile.html
|            |—— edit_profile.html
|            |—— view_profile.html
|        |—— recruiter
|            |—— all-applicants.html
|            |—— applicants.html
|            |—— dashboard.html
|            |—— recruiter_profile_add.html
|            |—— recruiter_profile_edit.html
|            |—— recruiter_profile_view.html
|            |—— recruiter_search.html
|        |—— recruiter_home.html
|        |—— search.html
```
## Code Details
### Tested Platform
- software
  ```
  OS: Debian unstable (May 2021), Ubuntu LTS
  Python: 3.8.5 (anaconda)
  PyTorch: 1.7.1, 1.8.1
  ```
- hardware
  ```
  CPU: Intel Xeon 6226R
  GPU: Nvidia RTX3090 (24GB)
  ```
### Hyper parameters
```
```
## References
- [paper-1]()
- [paper-2]()
- [code-1](https://github.com)
- [code-2](https://github.com)
  
## License

## Citing
If you use xxx,please use the following BibTeX entry.
```
```
