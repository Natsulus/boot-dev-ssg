import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.TEXT)
    node2 = TextNode("This is a text node", TextType.TEXT)
    self.assertEqual(node, node2)

  def test_repr(self):
    node = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual("TextNode(This is a text node, bold, None)", str(node))
    
  def test_default(self):
    node = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(None, node.url)
    
  def test_diff_type(self):
    node1 = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALIC)
    self.assertNotEqual(node1, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text(self):
    node = TextNode("Test", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "Test")
    
  def test_code(self):
    node = TextNode("insert code", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "insert code")
    
  def test_image(self):
    node = TextNode("image of boots", TextType.IMAGE, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "image of boots"})
  
  def test_link(self):
    node = TextNode("Go to Boot.dev", TextType.LINK, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Go to Boot.dev")
    self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

if __name__ == "__main__":
  unittest.main()