class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value
        self.children = children 
        self.props = props  

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return  ""
        return_string = ""
        for key in self.props:
            return_string += f' {key}="{self.props[key]}"'
        return return_string

    def __repr__(self):
        return f"The Object has the tag {self.tag}, the value {self.value}, the children {self.children} and the props {self.props}"