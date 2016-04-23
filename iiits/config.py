templates={
	"cms":{
		"image_slider":{
			"change":"iiits/cms/image_slider/change_image.html"
		},
		"admissions":{	
			"undergraduate":"iiits/cms/ug_admissions",
			"postgraduate":"iiits/cms/pg_admissions",
			"mtech":"iiits/cms/",
			"ms":"iiits/cms/",
			"phd":"iiits/cms/",
			"fee_structure":"iiits/cms/",
			"policy":"iiits/cms/",
			"financial_assistance":"iiits/cms/",
		},
		"academics":{	
			"change_time_table":"",
			"change_curriculum":"",
			"change_courses":"",
			"change_almanac":"",
		},
		"research":{
			"add_research_centre":"",
			"add_to_portfolio":"",
			"add_research_students":"",
			"add_publications":"",
			"change_research_centre_profile_description":"",
		},
		"campus_life":{

		},
		"news":{
			"add_news":"iiits/news/add.html"
		},
		"notice":{
			"add_notice":"iiits/notice/add.html"
		},
		"about":{
			"change_board_governers":"",
			"change_about_sricity":"",
			"change_reaching_iiit":"",
			"change_location":"",
			"add_developer":"",
		},


	},
	"site":{
		"academics":{
			"home":"iiits/site/academics/home.html",
			"curriculum":"iiits/site/academics/curriculum.html",
			"timetable":"iiits/site/academics/timetable.html",
			"general_info":"iiits/site/academics/general_info.html",
			"programmes":"iiits/site/academics/programmes.html"
		},
		"admissions":{
			"home":"iiits/site/admissions/home.html",
			"undergraduate":"iiits/site/admissions/undergraduate.html",
			"postgraduate":"iiits/site/admissions/postgraduate.html",
		},
		"alumni":{
			"home":"iiits/site/alumni/home.html",
			"list":"iiits/site/alumni/list.html"
		},
		"faculty":{
			"bio":"iiits/site/faculty/bio.html",
			"home":"iiits/site/faculty/home.html",
			"mast":"iiits/site/faculty/mast.html",
			"page":"iiits/site/faculty/page.html",
			"profile":"iiits/site/faculty/profile.html",
			"publications":"iiits/site/faculty/publications.html",
			"teaching":"iiits/site/faculty/teaching.html",
		},
		"news":{
			"home":"iiits/site/news/home.html"		
		},
		"notice":{
			"home":"iiits/site/notice/home.html"
		},
		"research":{
			"home":"iiits/site/research/home.html",
			"centres":"iiits/site/research/centres.html",
			"areas":"iiits/site/research/areas.html",
			"portfolio":"iiits/site/research/portfolio.html",
			"publications":"iiits/site/research/publications.html",
			"scholars":"iiits/site/research/scholars.html"
		},
		
		"site_image_slider":"",
		"site_navbar":"",
		"site_faculty_page":"",
		"site_faculty_list":"",
		"site_faculty_profile":"",
		"site_newsroom":"",
		"site_media":"",
		"site_students_page":"",
		"site_students_profile":"",
		"site_staff_list":"",
		"site_":""
	},
	"base":{
		"admissions":"iiits/base/base_admissions.html",
		"academics":"iiits/base/base_academics.html",
		"faculty":"iiits/base/base_faculty.html",
		"research":"iiits/base/base_research.html",
		"alumni":"iiits/base/base_alumni.html",
		"news":"iiits/base/base_alumni.html"
	}
}

urls={
	"cms":{
		"news":{
			"add_success":"/success/add/newsroom/"
		},
		"notice":{
			"add_success":"/success/add/notice/"
		}
	}
}	
values={
	"IMAGE_SLIDER_MAX_PHOTOS":"5",
	"PROFILE_PAGINATION_MAX_ENTRIES":"10",
	"NEWS_PAGINATION_MAX_ENTRIES":"5",
	"ACADEMICS_BATCHES": (
        ('UG1SEM1','UG1 Semester-1'),
        ('UG1SEM2','UG1 Semester-2'),
 	    ('UG2SEM3','UG2 Semester-3'),
 	    ('UG2SEM4','UG2 Semester-4'),
        ('UG3SEM5','UG3 Semester-5'),
        ('UG3SEM6','UG3 Semester-6'),
        ('UG4SEM7','UG4 Semester-7'),
        ('UG4SEM8','UG4 Semester-8')
    ),
    "ACADEMICS_BATCHES_DEFAULT":('UG1SEM1','UG1 Semester-1'),
    "ACADEMICS_BRANCHES":(
    	('CSE','Computer Science Engineering'),
    	('ECE','Electronics and Communications Engineering')
    ),
    "ACADEMICS_BRANCHES_DEFAULT":('CSE','Computer Science Engineering'),
    "ACADEMICS_SESSION":(
    	('MONSOON','Monsoon'),
    	('MONSOON','Spring')
    ),
    "ACADEMICS_SESSION_DEFAULT":('MONSOON','Monsoon'),
    "ACADEMICS_RESOURCES":(
    	('CALENDAR','Academic Calendar'),
    	('HOLIDAYS','Holidays'),
    	('Almanac','Almanac'),
    	('CURRICULUM_UG1_SEM1', 'UG1 Semester-1 Curriculum'),
    	('CURRICULUM_UG1_SEM2', 'UG1 Semester-2 Curriculum')
    ),
    "ACADEMICS_RESOURCES_DEFAULT":('CALENDAR','Academic Calendar'),
    "NOTES":(('FEE','Fee Payment'),
    		  ('POLICY','Admissions Policy'),
    		 ('ACADEMIC_PROGRAMMES','Academic Programmes'),
    		 ('UG_CURRICULUM','Under Graduate Curriculum'),
    		 ('UG_CURRICULUM_BENCHMARKING','Under Graduate Curriculum Benchmarking'),
    ),
    "NOTES_DEFAULT":('FEE','Fee Payment'),
    "YEAR":(
    	('2013','2013'),
    	('2014','2014'),('2015','2015'),
    	('2016','2016'),('2017','2017'),
    	('2018','2018'),('2019','2019'),
    	('2020','2020'),('2021','2021'),
    	('2022','2022'),('2023','2023'),
    	('2024','2024'),('2025','2025'),
    	('2026','2026'),('2027','2027'),
    	('2028','2028'),('2029','2029'),
    	('2030','2030'),('2031','2031'),
    	('2032','2032'),('2033','2033'),
    ),
    "YEAR_DEFAULT":('2016','2016'),
}
strings={
	"site_title":"IIITS - Indian Institute of Information Technology Chittoor, SriCity",
	"admissions_title":"Admissions @ IIITS",
	"academics_title":"Academics @ IIITS",
	"research_title":"Research @ IIITS"
}
static_locations={
	"AcademicsTimeTable":"iiits/static/iiits/files/academics/timetables/",
	"AcademicsResources":"iiits/static/iiits/files/academics/resources/",
	"ResearchPortfolio":"iiits/static/iiits/files/research/portfolio/"
}