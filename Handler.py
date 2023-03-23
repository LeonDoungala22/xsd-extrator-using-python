#This code was developed by : Leon Doungala
#Date: 20 / 03 / 2023
#Place : Milan


from xmlschema import XMLSchema
import xml.etree.ElementTree as ET
import pandas as pd


import pandas as pd
import xml.etree.ElementTree as ET

def extractor_SimpleType(xsd_file, csv_outputName):
    xsd_file = xsd_file
    tree = ET.parse(xsd_file)

    # Get the root element of the XSD file
    root = tree.getroot()

    # Create empty lists for storing data
    element_names = []
    is_simple_type = []     
    restriction = []
    fractionDigits = []
    totalDigits = []
    minInclusive = []
    pattern = []
    enumerations = []
    minLength = []
    maxLength =[]    
    

    # Iterate through each element in the XSD file
    for elem in root.iter():
        
        # If element is a simpleType
        if elem.tag.endswith('simpleType'):
            name = elem.get('name')
            print("\nsimpletype :", name)
            
            # Store simpleType name in list
            element_names.append(name)
            
            # Store 'yes' in list to indicate simpleType
            is_simple_type.append("yes")
            
            # Store empty strings in lists for each sub-element
            restriction_base = ""
            fractionDigits_value = ""
            totalDigits_value = ""
            minInclusive_value = ""
            pattern_value = ""
            maxLength_value = []
            minLength_value =[]
            enumerations_values = [] 
            # simpleType
            for child in elem.iter():
                
               
                # restriction
                if child.tag.endswith('restriction'):
                    restriction_base = child.get('base')
                    
                    # restriction
                    for restric_child in child.iter():
                        
                        # fractionDigits
                        if restric_child.tag.endswith('fractionDigits'):
                            fractionDigits_value = restric_child.get('value')
                        
                        #totalDigits
                        elif restric_child.tag.endswith('totalDigits'):
                            totalDigits_value = restric_child.get('value')
                        
                        # minInclusive
                        elif restric_child.tag.endswith('minInclusive'):
                            minInclusive_value = restric_child.get('value')
                            
                        #pattern
                        elif restric_child.tag.endswith('pattern'):
                            pattern_value = restric_child.get('value')
                        
                        #maxLength
                        elif restric_child.tag.endswith('maxLength'):
                            maxLength_value = restric_child.get('value')
                        
                        #minLength
                        elif restric_child.tag.endswith('minLength'):
                            minLength_value = restric_child.get('value')
                        
                        #enumeration
                        elif restric_child.tag.endswith('enumeration'):
                            enumeration_value = restric_child.get('value')
                            print("enumeration value:", enumeration_value)
                            enumerations_values.append(enumeration_value)
                            
                        
                        
                 
           
            
            # values in corresponding lists
            restriction.append(restriction_base)
            fractionDigits.append(fractionDigits_value)
            totalDigits.append(totalDigits_value)
            minInclusive.append(minInclusive_value)
            pattern.append(pattern_value)
           
            
            if enumerations_values:
                enumerations.append(enumerations_values)
            else:
                enumerations.append(None)
                
            if maxLength_value:
                 maxLength.extend([maxLength_value])
            else:
                maxLength.append(None)
            
            if minLength_value:
                minLength.extend([minLength_value])
            else:
                minLength.append(None)
                
            
                
      # Make sure all lists have the same length
    max_len = max(len(l) for l in [element_names, restriction, fractionDigits , totalDigits, minInclusive, pattern, enumerations, is_simple_type,maxLength,minLength])
    for l in [element_names, restriction, fractionDigits , totalDigits, minInclusive, pattern, is_simple_type,enumerations,maxLength,minLength]:
        if len(l) < max_len:
            l.extend([None] * (max_len - len(l)))
            

    # Create dictionary with lists as values
    data = {'Element Name': element_names, 
            'is_simple_type': is_simple_type, 
            'restriction base': restriction, 
            'fractionDigits value': fractionDigits,
            'totalDigits value': totalDigits , 
            'minInclusive value': minInclusive,
            'pattern':pattern,
            'minLength':minLength,
            'maxLength ': maxLength,
            'enumerations_values': enumerations
            
           }
    
   
    df = pd.DataFrame(data)
    
    
    #df = df.drop('is_simple_type', axis=1)
     
    df['restriction base'] = df['restriction base'].str.split(':').str[-1]
    
   

    df.to_csv(csv_outputName, index=False, header=True)

    print("Table saved to :", csv_outputName)

    return df




#complexType 

def extractor_complexType(xsd_file, csv_outputName):
    xsd_file = xsd_file
    tree = ET.parse(xsd_file)

    # Get the root element of the XSD file
    root = tree.getroot()

    # Create empty lists for storing data
    #element_names = []
    is_complexType_type = [] 

    
    
    #comptex types
    ComplextType=[]
    extension =[]
    attribute_n =[] #attribute name
    attribute_t =[] #attribute type
    attribute_u = [] # attribute use 
    attribute_type = []
    attribute_use =[]
    element_n=[]
    element_t=[]
    
    element_mOc =[]
    element_MOc = []
    

    # Iterate through each element in the XSD file
    for elem in root.iter():
        
        
        # complexType
        if elem.tag.endswith('complexType'):
            
            #comptex types
            attribute_name = []
            attribute_type = []
            attribute_use =[]
            extension_base=[]
                    
            comlexType_name =[]
            element_name=[]
            element_names=[]
            
            element_type =[]
            element_types=[]
            
            element_minOccur =[]
            element_minOccurs =[]
            
            element_maxOccur =[]
            element_maxOccurs =[]
            
            #Complextype Name
            comlexType_name = elem.get('name')
           # print("\ncomplexType :", comlexType_name)
            ComplextType.append(comlexType_name)
        
             
            # Store 'yes' in list to indicate complexType
            is_complexType_type.append("yes")
            
            #complextype
            for child in elem.iter():
                
                    #extension
                    if child.tag.endswith('extension'):
                        extension_base = child.get('base')
                        #print('extention base :',extension_base)

                        #iter into extextion tag
                        for restric_child in child.iter():

                                    # retrive attribute  name , type , use
                                    if restric_child.tag.endswith('attribute'):
                                        #name
                                        attribute_name = restric_child.get('name')
                                        #print('attribute name:',attribute_name)


                                        #type
                                        attribute_type = restric_child.get('type')
                                        #print("attribute type:",attribute_type)

                                        #use
                                        attribute_use = restric_child.get('use')
                                        #print("attribute use:",attribute_use)
                                        
                    #Element
                    elif child.tag.endswith('element'):
                        
                            #Element name 
                            element_name = child.get('name')
                            element_names.append(element_name)
                            #print('element name:',element_name)
                            
                            #Element type
                            element_type = child.get('type')
                            element_types.append(element_type)
                            #print('element type:',element_type)
                            
                            #Element minOccure
                            element_minOccur=child.get('minOccurs')
                            element_minOccurs.append(element_minOccur)
                            #print('element minOccure:',element_minOccur)
                            
                            #Elememnt maxOccure
                            element_maxOccur=child.get('maxOccurs')
                            element_maxOccurs.append(element_maxOccur)
                            #print('element MaxOccure:',element_maxOccur)
                                                                            
       
            # Store sub-element values in corresponding lists
            extension.append(extension_base)
            attribute_n.append(attribute_name)
            attribute_t.append(attribute_type)
            attribute_u.append(attribute_use)
           
            element_n.append(element_names)
            element_t.append(element_types)
            
            element_mOc.append(element_minOccurs)
            element_MOc.append(element_maxOccurs)
           
                           
            
                
            
                
      # Make sure all lists have the same length
    max_len = max(len(l) for l in [ComplextType, extension, attribute_n ,attribute_t,attribute_u,is_complexType_type,element_n,element_t,element_mOc,element_MOc])
    for l in [ComplextType, extension, attribute_n,attribute_t ,attribute_u,is_complexType_type,element_n,element_t,element_mOc,element_MOc]:
        if len(l) < max_len:
            l.extend([None] * (max_len - len(l)))
            

    data = {'ComplexType Name': ComplextType, 
            'is complexType type': is_complexType_type ,
            'extension base': extension,
            'attribute name':attribute_n,
            'attribute type':attribute_t,
            'attribute use':attribute_u,
            'element minOccur':element_mOc,
            'element maxOccure':element_MOc,
            'elements names':element_n,
            'elements types':element_t
           
            
           }
    
    # Create dataframe from dictionary
    df = pd.DataFrame(data)

     
    df['ComplexType Name'] = df['ComplexType Name'].str.split(',').str[-1]
    
    df.to_csv(csv_outputName, index=False, header=True)

    print("Table saved to :", csv_outputName)

    return df



#Format [] complextType

def FormatercomplexTtype(file_name,TBremove):
    #read data
    df = pd.read_csv(file_name)
    #convert into DataFrame
    df = pd.DataFrame(df)
    #Replace [] by None
    df=df.replace(TBremove,None)
    print("-",TBremove,"as been correctly handle..")
    #Update ouput file
    df.to_csv(file_name)
    print("-",file_name,"as been orrectlly update...\n\n")
    
    return df
    
   
