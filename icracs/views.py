from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    context = {
        "page_name": "Home"
    }
    return render(request, "icracs/index.html", context)

def about_view(request):
    context = {
        "page_name": "About"
    }
    return render(request, "icracs/about.html", context)

def contact_view(request):
    context = {
        "page_name": "Contact Us"
    }
    return render(request, "icracs/contact.html", context)

def dates_view(request):
    context = {
        "page_name" : "Dates"
    }
    return render(request, "icracs/dates.html", context)

def callforpaper_view(request):
    context = {
        "page_name" : "Call for paper"
    }
    return render(request, "icracs/callforpaper.html", context)

def papersubmission_view(request):
    context = {
        "page_name" : "Paper Submission"
    }
    return render(request, "icracs/papersubmission.html", context)

def commitee_view(request):
    conference_coordinaters = [
        {
            "member":"Dr. E. Sujatha"
            ,
            "profession":"Professor/CSE"
        },
        {
            "member":"Mr. P. V. Gopirajan",
            "profession":"Assistant Professor/CSE"
        },
        {
            "member":"Mr. N. Ravindhran"
            ,
            "profession":"Assistant Professor/CSE"
        },
        {
            "member":"Mr. Joel John"
            ,
            "profession":"Assistant Professor/CSE"
        },
        {
            "member":"Mrs. K. Niha"
            ,
            "profession":"Assistant Professor/CSE"
        }
    ]
    technical_commitee = [
        {"name":"Ricardo Verschueren",
        "profession":"Software Developer, RR Donnelley, Gloucestershire, UK"
        },
        {"name":"SubhodipMaulik",
        "profession":"Graduate Research Assistant, Louisiana State University, Baton Rouge, LA. U.S.A"
        },
        {"name":"Dr.Ho Soon Min",
        "profession":"Associate Professor, Mathematics and Sciences, INTI International University, Malaysia"
        },
        {"name":"Dr. Mohamed Abd El-Basset Matwalli",
        "profession":"Department of Operations Research & Decision Support System, Zagazig University, Egypt."
        },
        {"name":"DR.WilsonUdoUdofia",
        "profession":"Senior Lecture, College of Education, Afaha NSIT, AkwaIbom State, Nigeria."
        },

        {"name":"Mrs.SrismritaBasu",
        "profession":"Graduate Assistant, Louisiana State University, Baton Rouge, Louisiana, USA"
        },
        {"name":" Dr.AkmSamsur Rahman",
        "profession":"Assistant Professor,New York City College of Technology, USA"
        },
        {"name":"Dr.Eng.Hamid Ali Abed AL-Asadi",
        "profession":"Professor, Computer Science Department, Basra University,Iraq"
        },
        {"name":" Om Prakash Kumar",
        "profession":"Assistant Professor, Manipal Institute of Technology, Manipal"
        },
        {"name":"Dr. A. Heidari, Ph.D., D.Sc",
        "profession":"Faculty in California South University (CSU), USA."
        },
        {"name":"Prof.AnandNayyar",
        "profession":"Professor, KCL Institute of Management and Technology, Punjab, India."
        },
        {"name":"Dr. K.M. Subramanian",
        "profession":"Professor, Shadan College of Engineering and Technology, Hyderabad, India"
        },
        {"name":"Dr. S.Sivaramakrishnan",
        "profession":"Professor, ManakulaVinayagar Institute Of Technology, Puducherry, India."
        },
        {"name":"Dr.BOSELIN PRABHU S.R",
        "profession":"Professor, Sahrdaya College of Engineering and Technology, Kerala, India"
        },
        {"name":"MuralidharKurni",
        "profession":"Assosiate Professor, Anantha Lakshmi Institute of Technology &Sciences,AndhraPradesh,India"
        },
        {"name":"Dr. RajkumarBerwal",
        "profession":"Principal Investigator, College of Veterinary and Animal Science, Rajasthan, India"
        },
        {"name":"Dr.Uttam Kumar Roy",
        "profession":"Assistant Professor, Jadavpur University, Kolkata-700098, India"
        },
        {"name":"Prof.S.Balamurugan",
        "profession":"Professor, KalaignarKarunanidhi Institute of Technology, Coimbatore, India"
        },
        {"name":"Dr.Latha.R",
        "profession":"Associate Professor, Christ University, Karnataka, India"
        },
        {"name":"Dr.Uttam Kumar Roy",
        "profession":"Assosiate Professor, Jadavpur University, Kolkata, India"
        }
    ]
    review_commitee_ind = [
        {"name":"Prof. Anand Nayyar",
        "profession":"Professor, KCL Institute of Management and Technology, Punjab, India."
        },
        {"name":"Dr. K.M. Subramanian",
        "profession":"Professor, Shadan Coll Engineering and Technology, Hyderabad, India "
        },
        {"name":"Dr. S. Sivaramakrishnan",
        "profession":"Professor, Manakula Vinayagar Institute Of Technology, Puducherry, India"
        },
        {"name":"Dr. Boselin Prabhu",
        "profession":"SR. Professor, Sahrdaya College of Engineering and Technology, Kerala, India"
        },
        {"name":"Muralidhar Kurni",
        "profession":"Assosiate Professor, Anantha Lakshmi Institute of Technology &amp, Sciences,Andhra Pradesh, India"
        },
        {"name":"Dr. Rajkumar Berwal",
        "profession":"Principal Investigator, College of Veterinary and Animal Science, Rajasthan, India"
        },
        {"name":" Dr. Uttam Kumar Roy",
        "profession":"Assistant Professor, Jadavpur University, Kolkata-700098, India"
        },
        {"name":"Prof. S. Balamurugan",
        "profession":"Professor, Kalaignar Karunanidhi Institute of Technology. Coimbatore, India"
        },
        {"name":"Dr. R. Latha",
        "profession":"Associate Professor, Christ University, Karnataka, India"
        }
    ]
    review_commitee_int = [
        {"name":"Dr. A. Heidari, Ph.D., D.Sc",
        "profession":"Faculty in California South University (CSU), USA"
        },
        {"name":"Subhodip Maulik",
        "profession":"Graduate Research Assistant, Louisiana State University, Baton Rouge,LA. USA"
        },
        {"name":"Dr. Ho Soon Min",
        "profession":"Associate Professor, Mathematics and Sciences, INTI International University, Malaysia"
        },
        {"name":"Dr. Mohamed Abd El-Basset Matwalli",
        "profession":"Department of Operations Research &amp;Decision Support System, Zagazig University, Egypt."
        },
        {"name":"Dr. Wilson Udo Udofia",
        "profession":"Senior Lecture, College of Education, Afaha NSIT,Akwa Ibom State, Nigeria."
        },
        {"name":"Mrs. Sushmita Basu",
        "profession":"Graduate Assistant, Louisiana State University, Baton Rouge, Louisiana, USA "
        },
        {"name":"Dr. Akm Samsur Rahman",
        "profession":"Assistant Professor New York City College of Technology, USA"
        },
        {"name":"Dr. Eng. Hamid Ali Abed AL-Asadi",
        "profession":"Professor,Computer Science Department,Basta University,Iraq"
        },
        {"name":"Om Prakash Kumar",
        "profession":"Assistant Professor,Manipal Institute of Technology, Manipal"
        },
        {"name":"Ricardo Verschueren",
        "profession":"Software Developer, RR Donnelley, Gloucestershire, UK"
        }
    ]
    context = {
        "page_name" : "Commitee",
        "technical_commitee":technical_commitee,
        "conference_coordinaters":conference_coordinaters,
        "review_commitee_int":review_commitee_int,
        "review_commitee_ind":review_commitee_ind
    }
    return render(request, "icracs/commitee.html", context)

def speakers_view(request):
    context = {
        "page_name" : "Speakers"
    }
    return render(request, "icracs/speakers.html", context)

def journalPublication_view(request):
    context = {
        "page_name" : "Journal Publication"
    }
    return render(request, "icracs/journalPublication.html", context)