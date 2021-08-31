melodilinjer = 8.25e+19
komponertmsg = "Hvor mange ulike ti-toners melodilinjer tror du at du har hørt? "
komponert = float(input(komponertmsg))
prosent = (komponert / melodilinjer)*100
print(
    f"Det var mange... \nmen du har bare hørt {prosent:.2e} prosent av alle mulige melodier!")
