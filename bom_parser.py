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
                item.name = ls[self.categories["part"]] if (self.categories["part"] < rowLength) else ""

                # Unit cost.
                if ("unit cost" in self.categories and self.categories["unit cost"] < rowLength):
                    # check formatting of cost.
                    cost = ls[self.categories["unit cost"]]
                    item.cost = self.__formatNumber(cost)
                else:
                    item.cost = 0;

                # Vendor.
                if ("vendor" in self.categories and self.categories["vendor"] < rowLength):
                    item.vendor = ls[self.categories["vendor"]]
                else:
                    item.vendor = ""

                # Quantity to order.
                if("quantity to order" in self.categories and self.categories["quantity to order"] < rowLength):
                    item.quantity_to_order = int(ls[self.categories["quantity to order"]])
                else:
                    item.quantity_to_order = 0;

                # Part number.
                if("part number" in self.categories and self.categories["part number"] < rowLength):
                    item.part_number = ls[self.categories["part number"]]
                else:
                    item.part_number = ""

                # Website.
                if("website" in self.categories and self.categories["website"] < rowLength):
                    item.website = ls[self.categories["website"]]
                else:
                    item.website = ""

                # Notes.
                if("notes" in self.categories and self.categories["notes"] < rowLength):
                    item.notes = ls[self.categories["notes"]]
                else:
                    item.notes = ""

                self.items.append(item)
                #print i.name

    def getItems(self):
        for i in self.items:
            print i.cost
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
