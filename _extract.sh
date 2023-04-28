find ./ -name '*.xml' -exec itstool -l 'zh_Hant' -o ./description.pot {} +;
pogrep --search=notes -e '(\/en)$' -i ./description.pot -o ./description_en.pot
pot2po -i ./description_en.pot -o ./locals/description_zh_Hant_empty.po
