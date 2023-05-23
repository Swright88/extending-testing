# Test cases relating to the State transition Table 

* Please Note: Target refers to a name and address in the following document.

Before starting testing, I can see that there is no dropslist currently. This should be created by our programming when it is first utilised. 

1
* Start: Target Added to Originals

* Target is in droplist

* Target dropped

* Target not in Finals as has been dropped


2
* Start: Target added to Originals

* Target is in allowlist so continues

* Updated version of Target in updates

* Up to date version of Target added to Finals


3
* Start: No Target in Originals

* Target in droplist but no Target in Originals to drop

* Target IS in Upates

* Target added to Finals from Updates


4
* Start: Target in Originals

* Target not in droplist, different Target is in doplist

* No Target in Updates

* Target from Originals added to Finals as no Update available