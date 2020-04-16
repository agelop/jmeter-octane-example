import sys
import lxml.etree as ET

xml_jmeter_in=sys.argv[1]
xsl_convert=sys.argv[2]
xml_junit_out=sys.argv[3]

JMeterXML = ET.parse(xml_jmeter_in)
xsltConverter = ET.parse(xsl_convert)
transformXML = ET.XSLT(xsltConverter)
WellformattedJUnitXML = transformXML(JMeterXML)

#print(WellformattedJUnitXML)
f=open(xml_junit_out, "w")
f.write(str(WellformattedJUnitXML))
f.close()