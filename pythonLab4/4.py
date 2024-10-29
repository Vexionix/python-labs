def build_xml_element(tag, content, **key_values):
    key_value = ' '.join(key+"=\""+value+"\"" for key, value in key_values.items())
    return "<" + tag + " " + key_value + " > " + content + " <" + tag + "/>"

print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))