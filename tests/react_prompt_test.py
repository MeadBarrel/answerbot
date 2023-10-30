import unittest

from react_prompt import FunctionalReactPrompt, TextReactPrompt


class TestReactPrompt(unittest.TestCase):

    def test_functional_react_prompt_initialization(self):
        frprompt = FunctionalReactPrompt("Bla bla bla", 300)
        self.assertIn("Bla bla bla", frprompt.to_text())
        self.assertIn("For the Action step you can call the available functions.", frprompt.to_text())

    def test_text_react_prompt_initialization(self):
        trprompt = TextReactPrompt("Bla bla bla", 300)
        self.assertIn("Bla bla bla", trprompt.to_text())
        self.assertIn("After each observation, provide the next Thought and next Action. Here are some examples:",
                      trprompt.to_text())

    def test_react_prompt_examples_chunk_size(self):
        frprompt_small = FunctionalReactPrompt("Test chunk size", 150)
        frprompt_large = FunctionalReactPrompt("Test chunk size", 450)

        # This is a simple test to check if the larger chunk size results in a longer text.
        # You may need a more precise test depending on your actual implementation.
        self.assertTrue(len(frprompt_large.to_text()) >= len(frprompt_small.to_text()))

    # ... add more tests as necessary ...


if __name__ == '__main__':
    unittest.main()
