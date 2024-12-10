import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    props = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }
    node = HTMLNode("p", "hi", None, props)
    self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

  def test_repr(self):
    node = HTMLNode("p", "hi", None, {"test": "p_value"})
    self.assertEqual(node.__repr__(), "HTMLNode(p, hi, None, {'test': 'p_value'})")
  
  def test_default(self):
    node = HTMLNode()
    self.assertEqual(str(node), "HTMLNode(None, None, None, None)")

class TestLeafNode(unittest.TestCase):
  def test_no_value(self):
    node = LeafNode("p", None)
    self.assertRaises(ValueError, node.to_html)

  def test_no_tag(self):
    node = LeafNode(None, "test")
    self.assertEqual("test", node.to_html())
  
  def test_to_html(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
  def test_to_html(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )

    self.assertEqual(
      node.to_html(),
      "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
      )

  def test_nested_parents(self):
    node = ParentNode(
      "p",
      [
        ParentNode("p",
                    [
                      LeafNode(None, "Nested Normal text"),
                      LeafNode("i", "Nested italic text"),
                      ParentNode("p",
                                  [
                                    LeafNode(None, "DoubleNested"),
                                    LeafNode("b", "DoubleNested Bold")
                                  ])
                    ]),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )

    self.assertEqual(
      node.to_html(),
      "<p><p>Nested Normal text<i>Nested italic text</i><p>DoubleNested<b>DoubleNested Bold</b></p></p>Normal text<i>italic text</i>Normal text</p>"
      )
  def test_no_children(self):
    node = ParentNode("a", None)
    
    self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
  unittest.main()