import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("import.java.developer.vipin@gmail.com","Vipin#59")


subject="Sending........"
body="this is me . you are the best"

message="Subject:{}\n\n{}".format(subject,body)

listOfAddress=["vipinshrivastava59@gmail.com","vipinshrivastava92@gmail.com","vipinshrivastava310@gmail.com"]
ob.sendmail("IamOneDeveloper",listOfAddress,message)

ob.quit()
