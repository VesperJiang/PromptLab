import unittest

from src.prompt_analyzer import diagnose_prompt, score_prompt
from src.prompt_optimizer import explain_optimization, optimize_prompt


class BackendTestCase(unittest.TestCase):
    def test_score_prompt_returns_expected_keys(self):
        result = score_prompt(
            "You are a writing assistant. Write a short Markdown list for students."
        )

        self.assertIn("score", result)
        self.assertIn("problems", result)
        self.assertIn("dimension_scores", result)
        self.assertIn("feedback", result)
        self.assertIsInstance(result["score"], int)
        self.assertIsInstance(result["problems"], list)
        self.assertIsInstance(result["dimension_scores"], dict)
        self.assertIsInstance(result["feedback"], list)

    def test_diagnose_prompt_detects_short_prompt_problem(self):
        problems = diagnose_prompt("Help me")

        self.assertTrue(problems)
        self.assertTrue(any("Clarity" in problem for problem in problems))

    def test_optimize_prompt_supports_existing_app_call(self):
        optimized = optimize_prompt("Help me write about AI.")

        self.assertIn("Original request:", optimized)
        self.assertIn("Help me write about AI.", optimized)
        self.assertIn("Instructions:", optimized)

    def test_optimize_prompt_uses_passed_diagnosis(self):
        optimized = optimize_prompt(
            "Summarize this.",
            ["Context: Missing background or context."],
        )

        self.assertIn("Ask for missing background", optimized)

    def test_explain_optimization_supports_optional_diagnosis(self):
        explanations = explain_optimization(
            ["Task: The task is not clear enough."]
        )

        self.assertIn(
            "Made the task easier for the AI model to execute.",
            explanations,
        )


if __name__ == "__main__":
    unittest.main()
