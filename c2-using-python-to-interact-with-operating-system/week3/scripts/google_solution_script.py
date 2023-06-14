#!/usr/bin/env python3

import csv
import re

def contains_domain(address, domain):
    """This function uses regex to identify
    the domain of the user email addresses
    in the user_emails.csv file.
    Function checks, if an email address 
    belongs to the old domain (abc.edu)."""
    domain_pattern = r'[\w\.-]+@'+domain+'$'
    if re.match(domain_pattern, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Function replaces in the email addres
    the old domain name with a new domain name."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address
    
    
def main():
    """Processes the list of emails, replacing
    any instances of the old domain with the new domain."""
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_location = '../data/user_emails.csv'
    report_file = '../data/google_updated_user_emails.csv'
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []
    
    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        print("INITIAL user_data_list:")
        print(user_data_list)
        user_email_list = [data[1].strip() for data in user_data_list[1:]]
        
        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)
        
        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)
        
        for user in user_data_list[1:]:
            for old_domain_email, new_domain_email in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain_email:
                    user[email_index] = ' ' + new_domain_email
    f.close()
    
    with open (report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()
    

main()