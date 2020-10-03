import os
from flask import Flask , flash, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
import PyPDF2
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/pdf'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        def retrieve_name(text):
    
            name = text.partition('\n')[0]
            phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)
    
            if phone:
                number = ''.join(phone[0])
                if len(number) > 10:
                    number =  '+' + number 
                else:
                    number =  number 
            

            email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
            if email:
                try:
                    email =  email[0].split()[0].strip(';')
                except IndexError:
                    return None
            edu = []
            EDUCATION = [
                'BE','B.E.', 'B.E', 'BS', 'B.S', 
                'ME', 'M.E', 'M.E.', 'MS', 'M.S', 
                'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 
                'SSC', 'HSC', 'CBSE', 'ICSE','Bachelor','Master','PhD','BSc','BSc.'
            ,'investments','A.A.','A.S.','AAS','B.A','B.S.','BFA','BAS','MBA','MFA','Ph.D','Ph.D.','J.D','J.D.','M.D.','M.D','DDS','Diploma','diploma','Certificate','certficate','Certification','certification']
            eq = ''
            testt = text.split('\n')
            i = 0
            l = 0 
            k = len(EDUCATION)
            temp = 0
            for j in testt:
                    for k in EDUCATION:
                            if(k in j):
                                if(j not in edu):
                                    edu.append(j)
            
            edu_q = (''.join(edu))



            languages =[]
           
            language_list = ['Pidgin','Creole','Mandarin','Spanish','English','Hindi','Arabic','Portuguese','Russian','German','Korean','French','Italian','Polish','Hausa','Amharic','Romanian','Igbo','Dutch','Kurdish','Greek','Sylheti','Zulu','Czech','Haitian Creole','Swedish','Xhosa','Belarusian','Balochi','Konkani']
            
           
        
            temp = 0
            for l in testt:
                    for k in language_list:
                            if(k in l):
                                    languages.append(k)
            
            languages = set(languages)


            skills_listt =[]
           
            skills = ['JIRA','Zendesk','Salesforce','MS Office','Google Drive','Agile','Managing Cross-Functional Teams','Scrum','Performance Tracking','Financial Modelling','Ideation Leadership','Feature Definition','Forecasting','Profit and Loss','Scope Management','Project Lifecycle Management','A/B Testing','Social Media Marketing','Sales Funnel Management','Graphic Design Skills','Email Marketing','Email Automation','Photography','CAD','Design','Prototyping','Testing','Troubleshooting','Project Launch','Lean Manufacturing','Workflow Development','SolidWorks','Budgeting','Technical Report Writing','Time management','Data analysis','Web analytics','HTML & CSS','Wordpress','Email marketing','Web scraping','A/B Testing','Data visualization','pattern-finding','Search Engine','Keyword Optimization','Project/campaign management','B2B Marketing','Brand management','Creativity','Copywriting','Six Sigma techniques','The McKinsey 7s Framework','Porter’s Five Forces','PESTEL','Emotional Intelligence','People management','Business Development','Strategic Management','Negotiation' ,'Planning','Proposal writing','Customer Relationship Management','Cold-calling','Negotiation','Public speaking','Closing','Lead generation','Buyer engagement','Teamwork','Time management','Adobe Creative Suite', 'Illustrator', 'InDesign', 'Photoshop','Dreamweaver','Infographics','Photo editing','Typography','Storyboarding','Logo creation','Interactive media design','Ad design','Enterprise Resource Planning' ,'Big Data','Cognos Analytics','VBA','Visual Basic','Numerical competence','HTML','CSS','Javascript','Wordpress','Graphic User Interfaces','Git','Version control','Github', 'gitlab','Search Engine Optimization','SEO','Application Programming Interface','API','Adobe Photoshop', 'InDesign','Content Management Systems','CMS','Testing','Debugging','Responsive design','SQL','R', 'Python', 'Scala', 'Matlab','STATA', 'SPSS', 'SAS','Data Mapping','Entity Relationship Diagrams','Wireframes','Big Data' ,'Microsoft Visio','Agile Business Analysis','Machine learning','System Context Diagrams','Business Process Modeling','Technical and non-technical communication','Active listening','Communication','Computer skills','Customer service','Interpersonal skills','Leadership','Management skills','Problem-solving','Time management','Programming','Data Structures', 'Systems Programming', 'Algorithms','Object Oriented Systems Design', 'Switching and Finite Automata', 'Theory of Compiler Design','Linear Algebra', 'Modern Algebra', 'Operations','Python', 'C', 'C++', 'Java' ,'OpenCV', 'Scikit-learn', 'Matplotlib', 'Numpy', 'Scipy','Database',' MySQL' ,'Microsoft Oce','Adobe Suite', 'MATLAB', 'GIT','Data Analytics ','Power BI', 'Web Development ', 'Robotics' , 'Systems Administration' ,'IT Infrastructure ',' Motion Graphics' ,'Typography', 'Java','Tableau',' PHP', 'Adobe','MySQL', 'SQL', 'C#', 'JavaScript', 'C++', 'Python', 'iOS/Swift', 'Ruby on Rails','System administration', 'network configuration',' software installation',' security',' Cisco',' tech support',' updates',' project management',' research',' vendor management',' TCI/IP', 'DNS',' DHCP', ' WAN/LAN', 'Windows', 'Linux/Unix', 'Ubuntu', 'virtualized networks', 'network automation', 'cloud management', 'AI/machine learning','Web development','Microsoft Office','Project Scheduling','Strategic Planning','Subject Matter Expertise','Project Lifecycle Management','Agile Software','Scrum Management','Meeting Facilitation','Financial Modelling','Kanban','Forecasting','Lean Thinking','Performance Tracking','Budgeting', 'open source', 'data structures', 'coding', 'security', 'machine learning', 'debugging','Photoshop', 'Illustrator', 'InDesign', 'Acrobat', 'Corel Draw', 'HTML/CSS','Ruby','Agile','Scrum','MS Office','Microsoft Office','Excel','Powerpoint','Access','Photoshop', 'Salesforce (CRM)',' Oracle Netsuite (ERP)','InDesign','Profit & loss analysis', 'Technical writing',' research', 'leadership','employeee training','Supplier management', 'account management','MySQL', 'WordPress','Oracle','Data processing', 'Teradata', 'IBM DB2','Microsoft Access',' Cloud Computing','Artificial Intelligence','Analytical Reasoning','People Management','UX/UI','UX Design','Mobile Application Development','Video Production','Sales Leadership','Translation','Audio Production','Natural Language Processing','Scientific Computing','Game Development','Social Media Marketing','Animation','Business Analysis','Journalism','Digital Marketing','Industrial Design','Competitive Strategies','Customer Service Systems','Software Testing','Data Science','Computer Graphics','Corporate Communications']
            
            
        
            temp = 0
            for j in testt:
                    for k in skills:
                            if(k in j):
                                    skills_listt.append(k)
            
            skills_listt = set(skills_listt)




            joblist =[]
           
            job_titles=['Consultant','Advisor','Intern','Web Designer','President','Project Manager','Librarian','Project Manager','Marketing Specialist','Marketing Manager','Marketing Director','Graphic Designer','Marketing Research Analyst','Marketing Communications Manager','Marketing Consultant','Product Manager','Public Relations','Social Media Assistant','Brand Manager','SEO Manager','Content Marketing Manager','Copywriter','Digital Marketing Manager','eCommerce Marketing Specialist','Brand Strategist','Vice President of Marketing','Media Relations Coordinator','Administrative Assistant','Receptionist','Office Manager','Auditing Clerk','Branch Manager','Business Manager','Quality Control Coordinator', 'Administrative Manager','Chief Executive Officer','Business Analyst',' Risk Manager','Human Resources','Office Assistant','Secretary','Office Clerk','File Clerk','Account Collector','Administrative Specialist','Executive Assistant','Program Administrator','Program Manager','Administrative Analyst','Data Entry','CEO','Chief Executive Officer','COO','Chief Operating Officer','CFO','Chief Financial Officer','CIO','Chief Information Officer','CTO','Chief Technology Officer','CMO','Chief Marketing Officer','CHRO','Chief Human Resources Officer','CDO','Chief Data Officer','CPO','Chief Product Officer','CCO',' Chief Customer Officer','Manager','Assistant Manager','Executive','Director','Coordinator','Administrator','Controller','Officer','Organizer','Supervisor','Superintendent','Head','Overseer','Chief','Foreman','Controller','Principal','President','Lead','Computer Scientist','IT Professional','UX Designer & UI Developer','UX Designer','SQL Developer','Web Designer','Web Developer','Desktop Support','Software Engineer','Data Entry','DevOps Engineer','Computer Programmer','Network Administrator','Information Security Analyst','Artificial Intelligence Engineer','Cloud Architect','IT Manager','Technical Specialist','Application Developer','Chief Technology Officer','CTO','Chief Information Officer', 'CIO','Sales Associate','Sales Representative','Sales Manager','Retail Worker','Store Manager','Sales Representative','Sales Manager','Real Estate Broker','Sales Associate','Cashier','Store Manager','Account Executive','Sales Analyst','Market Development Manager','B2B Sales Specialist','Sales Engineer','Proprietor','Principal','Owner','President','Founder','Administrator','Director','Managing Partner','Managing Member','Associate','Analyst','Board of Directors','Quality Control','Human Resources','Shipping and Receiving Staff','Office Manager','Receptionist','Operations Manager','Operations Assistant','Operations Coordinator','Operations Analyst','Operations Director','Vice President of Operations','Operations Professional','Scrum Master','Accountant','Accounting Analyst','Accounting Director','Accounts Payable/Receivable Clerk','Auditor','Budget Analyst','Controller','Financial Analyst','Finance Manager','Economist','Payroll Manager','Payroll Clerk','Financial Planner','Financial Services Representative','Finance Director','Commercial Loan Officer','Engineer','Mechanical Engineer','Civil Engineer','Electrical Engineer','Assistant Engineer','Chemical Engineer','Biological Engineer','Maintenance Engineer','Mining Engineer','Nuclear Engineer','Petroleum Engineer','Plant Engineer','Production Engineer','Quality Engineer','Safety Engineer','Sales Engineer','Researcher','Research Assistant','Data Analyst','Business Analyst','Financial Analyst','Biostatistician','Market Researcher','Title Analyst','Medical Researcher']
            
        
            temp = 0
            for jt in testt:
                    for k in job_titles:
                            if(k in jt):
                                    joblist.append(jt)
            
            joblist = set(joblist)



            country_listt =[]
           
            country = ['Afghanistan','Albania','Algeria','United Sates of America','Andorra','Angola','Anguilla','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Britain','British Virgin Islands','Brunei','Bulgaria','Burkina Faso','Burma','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Cayman Islands','Central African Republic','Chad','Chile','China','Colombia'	,'Comoros','Congo','Cook Islands','Costa Rica','Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominican Republic','Dominican Republic','Netherlands','East Timor','Ecuador','Egypt','United Arab Emirates','England','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Faroe Island','Fiji','Philipines','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland','Grenada','Guaman','Guatemala','Guinea-Bissau','Guinea','Guyana','Haiti','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Ivory Coast','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kosovo','Kuwait','Kyrgyzstan','Lao','Latvia','Lebanon','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Malawi','Malaysia','Maldives','Mali','Malta','Mauritania','Mauritius','Mexico','Moldova','Mongolia','Montenegro','Montserra','Morocco','Mosotho','Mozambique','Namibia','Nepal','New Zealand','Nicaragua','Niger','Nigeria','North Korean','Northern Ireland','Norway','Oman','Pakistan','Palau','Palestine','Panama','Papua New Guinea','Paraguay','Peru','Pitcairn Island','Poland','Portugal','Puerto Rico','Qatar','Romania','Russia','Rwanda','Salvador','Sammarine','Samoa','Sao Tome','Saudi Arabia','Scotland','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka','St Helenia','St Lucia','Sudan','Surinam','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikstan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tristania','Tunisia','Turkey','Turkmen Turks and Caicos Islands','Tuvalu','Uganda','Ukraine','Uruguay','Uzbekistan','Vatican City','Vanuatu','Venezuela','Vietnam','St. Vincent',	'Wales','Yemen','Zambia','Zimbabwe']
            
            
        
            temp = 0
            for j in testt:
                    for k in country:
                            if(k in j):
                                    country_listt.append(k)
            
            country_listt = set(country_listt)




            nationality_listt =[]
           
            nationality = ['Afghan','Albanian','Algerian','American','Andorran','Angolan','Anguillan','Citizen of Antigua and Barbuda','Argentine','Armenian','Australian','Austrian','Azerbaijani','Bahamian','Bahraini','Bangladeshi','Barbadian','Belarusian','Belgian','Belizean','Beninese','Bermudian','Bhutanese','Bolivian','Citizen of Bosnia and Herzegovina','Botswanan','Brazilian','British','British Virgin Islander','Bruneian','Bulgarian','Burkinan','Burmese','Burundian','Cambodian','Cameroonian','Canadian','Cape Verdean','Cayman Islander','Central African','Chadian','Chilean','Chinese','Colombian'	,'Comoran Congolese','Congolese','Cook Islander','Costa Rican','Croatian','Cuban','Cymraes','Cymro','Cypriot','Czech','Danish','Djiboutian','Dominican','Citizen of the Dominican Republic','Dutch','East Timorese','Ecuadorean','Egyptian','Emirati','English','Equatorial Guinean','Eritrean','Estonian','Ethiopian','Faroese','Fijian','Filipino','Finnish','French','Gabonese','Gambian','Georgian','German','Ghanaian','Gibraltarian','Greek','Greenlandic','Grenadian','Guamanian','Guatemalan','Citizen of Guinea-Bissau','Guinean','Guyanese','Haitian','Honduran','Hong Konger','Hungarian','Icelandic','Indian','Indonesian','Iranian','Iraqi','Irish','Israeli','Italian','Ivorian','Jamaican','Japanese','Jordanian','Kazakh','Kenyan','Kittitian','Citizen of Kiribati','Kosovan','Kuwaiti','Kyrgyz','Lao','Latvian','Lebanese','Liberian','Libyan','Liechtenstein citizen','Lithuanian','Luxembourger','Macanese','Macedonian','Malagasy','Malawian','Malaysian','Maldivian','Malian','Maltese','Marshallese','Martiniquais','Mauritanian','Mauritian','Mexican','Micronesian','Moldovan','Monegasque','Mongolian','Montenegrin','Montserratian','Moroccan','Mosotho','Mozambican','Namibian','Nauruan','Nepalese','New Zealander','Nicaraguan','Nigerian','Nigerien','Niuean','North Korean','Northern Irish','Norwegian','Omani','Pakistani','Palauan','Palestinian','Panamanian','Papua New Guinean','Paraguayan','Peruvian','Pitcairn Islander','Polish','Portuguese','Prydeinig','Puerto Rican','Qatari','Romanian','Russian','Rwandan','Salvadorean','Sammarinese','Samoan','Sao Tomean','Saudi Arabian','Scottish','Senegalese','Serbian','Citizen of Seychelles','Sierra Leonean','Singaporean','Slovak','Slovenian','Solomon Islander','Somali','South African','South Korean','South Sudanese','Spanish','Sri Lankan','St Helenian','St Lucian','Sudanese','Surinamese','Swazi','Swedish','Swiss','Syrian','Taiwanese','Tajik','Tanzanian','Thai','Togolese','Tongan','Trinidadian','Tristanian','Tunisian','Turkish','Turkmen','Turks and Caicos Islander','Tuvaluan','Ugandan','Ukrainian','Uruguayan','Uzbek','Vatican citizen','Citizen of Vanuatu','Venezuelan','Vietnamese','Vincentian','Wallisian'	'Welsh','Yemeni','Zambian','Zimbabwean']
            
            
        
            temp = 0
            for j in testt:
                    for k in nationality:
                            if(k in j):
                                    nationality_listt.append(k)
            
            nationality_listt = set(nationality_listt)


            associations =[]
           
            associate = ['National','Academy','ACCA','Certified','Certified Public Accountants','Accountants','Association','Examiners','Professionals','Society','Civil Engineers','ASCE','CFA Institute','CFA','Board of Standards','Chartered Global','Management Accountants','CIMA','Chartered Management','Chartered Institute','Commission','Institute','Internal Auditors','International','Council','Institution','Union','Federation','Associations','International','Project Management Institute','PMI','Society','Institute']
            
        
            temp = 0
            for j in testt:
                    for k in associate:
                            if(k in j):
                                    associations.append(j)
            
            associations = set(associations)
            return render_template('processing.html', elist = skills_listt,edu=edu,pdf=pdf_location,name=name,languages=languages,country=country_listt,nationality=nationality_listt,email=email,number=number,joblist=joblist,associations=associations)
           
                                    
        
       
        def extract_text_from_pdf(pdf_path):
            
            
            for page in PDFPage.get_pages(pdf_path, caching=True, check_extractable=True):
                # creating a resoure manager
                resource_manager = PDFResourceManager()
                
                # create a file handle
                fake_file_handle = io.StringIO()
                
                # creating a text converter object
                converter = TextConverter(
                                    resource_manager, 
                                    fake_file_handle, 
                                    codec='utf-8', 
                                    laparams=LAParams()
                            )

                # creating a page interpreter
                page_interpreter = PDFPageInterpreter(
                                    resource_manager, 
                                    converter
                                )

                # process current page
                page_interpreter.process_page(page)
                
                # extract text
                text = fake_file_handle.getvalue()
                yield(text)

                # close open handles
                converter.close()
                fake_file_handle.close()
                

        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pdf_location = filename
        text = ""
        for page in extract_text_from_pdf(file):
            text += ' ' + page

        return(retrieve_name(text))

        
        


         
    
# creating a pdf reader object  
          
      
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))



