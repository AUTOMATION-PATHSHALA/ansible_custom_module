
DOCUMENTATION = '''
module: get_area
short_description: Calculate area of triangle or rectangle
'''

EXAMPLES = '''
- name: Calculate area of triangle
  get_area:
    hight: 20
    breath: 30
    action: "area_of_triangle"
  register: get_area_of_triangle

- name: Calculate area of rectangle
  get_area:
    length: 20
    breath: 30
    action: "area_of_rectangle"
  register: get_area_of_rectangle

'''


from ansible.module_utils.basic import AnsibleModule

def area_of_rectangle(inputparam):
    try:
        length = inputparam['length']
        breath = inputparam['breath']

        return False, True, f"Area of rectangle : {str(int(length) * int(breath))}"
    except Exception as ex:
        return True, False, ex.message
    
def area_of_triangle(inputparam):
    try:
        hight = inputparam['hight']
        breath = inputparam['breath']

        return False, True, f"Area of triangle : {str((int(hight) * int(breath))/2)}"
    except Exception as ex:
        return True, False, ex.message
    
def module_message(inputparam):
    return True, False, "action parameter is required to perform get area of rectangle/triangle."

def main():
    fields = {
        "hight": {"type": str},
        "length": {"type": str},
        "breath": {"type": str},
        "action": {
            "default": "module_message",
            "type": str,
            "choices": ['module_message', 'area_of_rectangle', 'area_of_triangle'] 
        },
    }

    choice_map = {
        "area_of_rectangle": area_of_rectangle,
        "area_of_triangle": area_of_triangle,
        "module_message": module_message,
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = choice_map.get(module.params['action'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, result=result)
    else:
        module.fail_json(changed=has_changed, msg=result)

if __name__=='__main__':
    main()

