from constants import *
class Item:
    notes = ""
    name = ""
    cost = 0
    quantity_to_order = 0
    vendor = ""
    part_number = ""
    website = ""
class BomParser:

    def __init__(self, f_name):
        self.file_name = f_name
        self.items = []
        self.description = ""
        self.categories = {}

        f = open(self.file_name)

        # Map categories to column index (first line).
        ls = f.readline().strip()
        ls_array = ls.split('\t')
        print(ls)
        for i in range(len(ls_array)):
            self.categories[ls_array[i].lower()] = i;
        print(self.categories)

        # Parse the rest of the BOM.
        for line in f:
            ls = line.split('\t')
            # If valid row, then extract information into item.
            if self.__checkValidRow(ls):
                print(ls)
                item = Item()
                rowLength = len(ls)

                # Name.
                item.name = ls[self.categories[PART]] if (self.categories[PART] < rowLength) else ""

                # Unit cost.
                if (UNIT_COST in self.categories and self.categories[UNIT_COST] < rowLength):
                    # check formatting of cost.
                    cost = ls[self.categories[UNIT_COST]]
                    item.cost = self.__formatNumber(cost)
                else:
                    item.cost = 0;

                # Vendor.
                if (VENDOR in self.categories and self.categories[VENDOR] < rowLength):
                    item.vendor = ls[self.categories[VENDOR]]
                else:
                    item.vendor = ""

                # Quantity to order.
                if(QUANTITY_TO_ORDER in self.categories and self.categories[QUANTITY_TO_ORDER] < rowLength):
                    item.quantity_to_order = int(ls[self.categories[QUANTITY_TO_ORDER]])
                else:
                    item.quantity_to_order = 0;

                # Part number.
                if(PART_NUMBER in self.categories and self.categories[PART_NUMBER] < rowLength):
                    item.part_number = ls[self.categories[PART_NUMBER]]
                else:
                    item.part_number = ""

                # Website.
                if(WEBSITE in self.categories and self.categories[WEBSITE] < rowLength):
                    item.website = ls[self.categories[WEBSITE]]
                else:
                    item.website = ""

                # Notes.
                if(NOTES in self.categories and self.categories[NOTES] < rowLength):
                    item.notes = ls[self.categories[NOTES]]
                else:
                    item.notes = ""

                self.items.append(item)
                #print i.name

    def getItems(self):
        return self.items

    def getConcatDescription(self):
        return self.description

    # Check if there aren't enough filled cells.
    def __checkValidRow(self, ls):
        filledCells = 0
        for s in ls:
            if s != "":
                filledCells += 1
        if filledCells < 3:
            return False
        return True

    # Get rid of any special characters the string str_num has and convert to number.
    def __formatNumber(self, str_num):
        num = 0
        try:
            num = float(str_num)
        except ValueError: # Parse string into num
            if str_num[0] == "$":
                str_num = str_num[1:]
                num = float(str_num)
        return num
