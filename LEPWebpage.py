import streamlit as st


def main():
    st.title("LOAN PREDICTION")
    menu = ["home", "login", "signup"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "home":
        st.subheader("home")
    elif choice == "login":
        st.subheader("login section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.checkbox("login"):
            create_usertable()
            result = login_user(username, password)
            if result:
                st.success("Logged in as {}".format(username))

                task = st.selectbox("task", ["Loan", "Profile"])
                if task == "Loan":
                    def run():

                        st.title("Bank Loan Prediction using Machine Learning")

                        ## Account No
                        account_no = st.text_input('Account number')
                        if len(account_no) == 10:
                            ## Full Name
                            fn = st.text_input('Full Name')

                            ## For gender

                            gen_display = ("Not selected", 'Female', 'Male', "other")
                            gen_options = list(range(len(gen_display)))
                            gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

                            ## For Marital Status
                            mar_display = ("Not selected", 'No', 'Yes')
                            mar_options = list(range(len(mar_display)))
                            mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])
                            ## For Marital Status
                            mar_display = ("Not selected", 'No', 'Yes')
                            mar_options = list(range(len(mar_display)))
                            mar = st.selectbox("Marital Status", mar_options, format_func=lambda x:
                            mar_display[x])

                            ## No of dependets
                            dep_display = ("Not selected", 'No', 'One', 'Two', 'More than Two')
                            dep_options = list(range(len(dep_display)))
                            dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x])
                            ## For edu
                            edu_display = ("Not selected", 'Not Graduate', 'Graduate')
                            edu_options = list(range(len(edu_display)))
                            edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

                            ## For emp status
                            emp_display = ("Not selected", 'Job', 'Business')
                            emp_options = list(range(len(emp_display)))
                            emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

                            ## For Property status
                            prop_display = ("Not selected", 'Rural', 'Semi-Urban', 'Urban')
                            prop_options = list(range(len(prop_display)))
                            prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

                            ## For Credit Score
                            cred_display = ("Not selected", 'Between 300 to 500', 'Above 500')
                            cred_options = list(range(len(cred_display)))
                            cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

                            ## Applicant Monthly Income
                            mon_income = st.number_input("Applicant's Monthly Income(Rs/-)", value=0)
                            ## Co-Applicant Monthly Income
                            co_income = st.number_input("Co-Applicant's Monthly Income(Rs/)", value=0)

                            ## Loan Amount
                            loan_amt = st.number_input("Loan Amount(Rs/-)", value=0)

                            ## Loan Duration
                            dur_display = ["Not selected", '2 Month', '6 Month', '8 Month', '1 Year', '1Month']
                            dur_options = range(len(dur_display))

                            dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x])
                            if st.button("Submit"):
                                duration = 0
                                if dur == 0:
                                    duration = 60
                                if dur == 1:
                                    duration = 180
                                if dur == 2:
                                    duration = 240
                                if dur == 3:
                                    duration = 360
                                if dur == 4:
                                    duration = 480
                                features = [
                                    [gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred,
                                     prop]]
                                print(features)
                                prediction = model.predict(features)
                                if prediction == 'Y':
                                    ans = 1
                                else:
                                    ans = 0
                                    if ans == 0:
                                        st.error(
                                            "Hello: " + fn + " || ""Account number: " + account_no + '| | ' 'According to our   Calculations, you will not get the loan from Bank')
                                    else:
                                        st.success(
                                            "Hello: " + fn + " || ""Account number: " + account_no + ' | | ' 'Congratulations!! you will get the loan from Bank')

                        elif len(account_no) != 10:
                            print("invalid")

                    run()
                elif task == "Profile":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result, columns=["Username"])
                    st.dataframe(clean_db)

                else:
                    st.warning("Incorrect Username/Password")
    elif choice == "signup":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        mobile = st.text_input("Mobile Number")
        if st.button("signup"):
            create_usertable()
            add_userdata(new_user, new_password)
            st.success("You have successfully created a valid account")
            st.info("Go to Login menu to login")


main()