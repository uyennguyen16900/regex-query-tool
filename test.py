# {% set i = namespace(a=0) %}
# {% for word in test_str -%}
# {% if loop.index0 >= indices[i.a][0] and loop.index0 <= indices[i.a][1] %}
#   <div style="background-color:blue">
#     {{ word }}
#   </div>
#   {{indices[i.a][0]}}
# {% elif loop.index0 < (test_str|length) - 1 and loop.index0 == indices[i.a][1] + 1 %}
#   {% set i.a = i.a + 1 %}
# {% else %}
#   {{ word }}
# {% endif %}

def test(test_str, indices):
    i = 0
    for index, word in enumerate(test_str):
        print(i)
        if index >= indices[i][0] and index <= indices[i][1]:
            print(word + 'hightlight')

        elif i < len(indices) - 1 and index == indices[i][1] + 1:
            i = i + 1

        else:
            print(word)

indices = [(0, 5), (61, 67), (110, 113), (182, 186), (250, 253), (288, 294)]
test_str = ("Lorem ipsum dolor sit amet, nam no malis graecis incorrupte. Dicunt insolens sed ex, ut saepe quaerendum eam. Eum no quas tempor impetus, in per expetendis reprimique mediocritatem. Meis erant facilisi cu ius, utroque moderatius voluptatibus no nam. Pri an graecis torquatos accommodare. Quodsi everti ei qui")
print(test(test_str, indices))
