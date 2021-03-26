
def fbcs(d,s): #Find elements by class name
    return d.find_elements_by_class_name(s)

def fbc(d,s): #Find element by class name
    return d.find_element_by_class_name(s)

def fbct(d,c,t): #Find element by class name with exact text
    l = d.find_elements_by_class_name(c)
    el = d.find_element_by_class_name(c)
    found = False
    for els in l:
        if els.text == t:
            el = els
            found = True
    if found == True:
        return el
    else:
        return "Could not find"

def fbcss(d,s): #Find element by CSS selector
    return d.find_element_by_css_selector(s)

def fbxp(d,s): #Find element by XPath
    return d.find_element_by_xpath(s)

def fbi(d,s): #Find element by ID
    return d.find_element_by_id(s)

def fbtn(d,s): #Find element by HTML Tag
    return d.find_element_by_tag_name(s) 

def fbtns(d,s): #Find elements by HTML Tag
    return d.find_elements_by_tag_name(s) 

def fbtnt(d,s,t): #Find element by HTML Tag with exact text
    try:
        l = d.find_elements_by_tag_name(s) 
        el = d.find_element_by_tag_name(s)
        found = False
        for els in l:
            #print(els.text)
            if els.text == t:
                el = els
                found = True
        if found == True:
            return el
        else:
            return "Could not find"
    except:
        return "Could not find"

def fbtnit(d,s,t): #Find element by HTML Tag including text
    try:
        l = d.find_elements_by_tag_name(s) 
        el = d.find_element_by_tag_name(s)
        found = False
        for els in l:
            #print(els.text)
            if t in els.text:
                el = els
                found = True
        if found == True:
            return el
        else:
            return "Could not find"
    except:
        return "Could not find"

def fht(d): #?????
    l = d.find_elements_by_tag_name("a") 
    el = []
    found = False
    for els in l:
        #print(els.text)
        if "#" in els.text:
            el.append(els)
            found = True
    if found == True:
        return el
    else:
        return "Could not find"
 