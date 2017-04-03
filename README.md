BOM Parser
===============================================
A script for automating form completion from a .tsv file to the Viterbi RTHBC Purchase Request website.

Setup
-----------------------------------------------
* Python version 2.7.10 or higher
 * https://www.python.org/downloads/
* Selenium webdriver for Python version 3.0.0
 * https://pypi.python.org/pypi/selenium
* Google Chrome browser


Usage
-----------------------------------------------
1. Navigate to auto_bom directory.
 * For Mac:
 ```
 cd auto_bom
 ```
 * For PC:
 ```
 dir auto_bom
 ```
2. Run script in Terminal:
```
python main.py
```
3. Follow prompt to enter BOM path (this is a relative path).
 * Example:
 ```
 $ Path to BOM file (format .tsv): hot_wire_bom.tsv
 ```

Test
-----------------------------------------------
Test with 'hot_wire_bom.tsv':
```
$ python main.py
$ hot_wire_bom.tsv
```

BOM Keywords
-----------------------------------------------
Use these header labels in the BOM on the first line if you want them to be recognized by the script (case insensitive).

* Part : the name of the part you want to order.
* Unit cost : the unit cost.
* Vendor : the company selling this part.
* Quantity to order : how many units to order.
* Website : the website you should purchase from.
* Item number : the item number.

BOM formatting
-----------------------------------------------
* The parser will only consider a row as an item if it is 'complete'. Complete means that more than 2 cells have been filled in.
* Make sure the first row consists of the categories.
* Rows that don't have items should not have more than 2 cells filled in.
* Refer to 'hot_wire_bom.tsv' for an example.
