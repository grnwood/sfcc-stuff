# sfcc-stuff

A few tools.

## sfcc-partners.py
### Tired of going to the Salesforce Marketplace to look for a cartridge?
### If you don't want to use the only page on the internet (since pre Frontpage Extensions) that does not have a search capability, use this.

This will give you a quick way to see if it's worth even looking.

```
./sfcc-partners.py <search term>
```
  
Example, is there a Adyen cartridge?
```
$ .\sfcc-partners.py adyen
* Scraping page 10 pages.
[**********]
Adyen is the global payments platform of choice for the world   s leading companies.
Adyen is a technology company reinventing payments. We deliver frictionless payments across online, mobile, and in-store.
```

Is there a Social Annex cartridge?
```
$ .\sfcc-partners.py annex
* Scraping page 10 pages.
[**********]
Annex Cloud delivers fully integrated Customer Loyalty, Referral Marketing, and User Generated Content solutions.
Annex Cloud   s provides Customer Loyalty, Referral Marketing and User Generated Content solutions to boost your business.
```

  
