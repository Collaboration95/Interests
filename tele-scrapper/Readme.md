# Linkedin Scrapper using Telethon ? library

Some parameters i should think about 

results can be skewed by continuous conversations , therefore true wait time between conversations might be disproportionately

if characters are used as a parameter , messages having more than a limit of characters have to be deleted to avoid copypasta dirtying the data

or outliers can be found using IQR and the outliers can be deleted
but we have to fix IQR to be greater than 1.5 and not less than -1.5IQR to fix smaller messages getting wiped out 