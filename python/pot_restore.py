import polib
import xml.etree.ElementTree as ET

def main():
    locals_zh = 'locales/description_zh_Hant.po'
    zh_po = polib.pofile(locals_zh)

    for entry in zh_po:
        if len(entry.msgid) > 0:
            occurrences = entry.occurrences
            comment = entry.comment

            for location in occurrences:
                file_path, line_number = location
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()

                    for parent in root.findall('.//*'):
                        for en_tag in parent.findall('en'):
                            if entry.msgid == en_tag.text:
                                # 檢查是否已經有ZH
                                has_tag = parent.find('zh_Hant')
                                if has_tag == None:
                                    # 創建新的 'zh_Hant' 節點
                                    zh_hant_tag = ET.SubElement(parent, 'zh_Hant')
                                    zh_hant_tag.text = entry.msgstr

                    tree.write(file_path, encoding='utf-8', xml_declaration=True)

                except ET.ParseError:
                    print(f"Error parsing XML file: {file_path}")
                except FileNotFoundError:
                    print(f"File not found: {file_path}")


if __name__ == '__main__':
    main()