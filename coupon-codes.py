#! python3w

import xml.etree.ElementTree as ET
tree = ET.parse("C:/Users/jogreenw/AppData/Local/Temp/7zO0D747F01/coupons.xml")
root = tree.getroot()

for coupon in root.findall('coupon'):
    desc = coupon.find('description')
    if desc is not None:
        if (desc.text) == 'Home Delivery':
            cid = coupon.attrib['coupon-id']
            if not cid.startswith("HomeDelivery_"):
                cid = 'HomeDelivery_'+cid
            print("keeping: "+cid+':'+desc.text)
            coupon.attrib['coupon-id'] = cid
        else:
            root.remove(coupon)
    else:
        root.remove(coupon)

for cc in root.findall('coupon-codes'):
    root.remove(cc)

tree.write("C:/Users/jogreenw/AppData/Local/Temp/7zO0D747F01/coupons-hd.xml")
    
