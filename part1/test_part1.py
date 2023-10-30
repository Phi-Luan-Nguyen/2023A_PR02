import os
import unittest
import nbformat
import pandas as pd

FUNCTION_NAMES = ['create_pokedex', 'filter_columns',
                  'rename_columns', 'clean_data', 'correct_columns_types']


def import_notebook_functions(notebook_path, function_names):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = f.read()

    notebook = nbformat.reads(notebook_content, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type == "code":
            for function_name in function_names:
                if f"def {function_name}(" in cell.source:
                    exec(cell.source, globals())
                    break


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

import_notebook_functions(f"{CURRENT_DIR}/analysis.ipynb", FUNCTION_NAMES)


class TestPokedexAnalysis(unittest.TestCase):

    columns_to_keep = ["name", "type1", "type2", "attack", "defense", "sp_attack", "sp_defense", "hp", "speed",
                       "generation", "is_legendary"]

    def setUp(self):
        self.df = create_pokedex()

    def test_create_pokedex(self):
        self.assertEqual(pd.DataFrame, type(self.df))
        self.assertEqual((807, 41), self.df.shape)

    def test_filter_columns(self):
        filter_columns(self.df)
        self.assertEqual((807, 11), self.df.shape)
        self.assertEqual(set(self.columns_to_keep), set(self.df.columns))

    def test_rename_columns(self):
        columns = self.df.columns
        rename_columns(self.df)
        new_columns = ['Name', 'Primary Type', 'Secondary Type', 'Attack', 'Defense', 'Special Attack',
                       'Special Defense', 'HP', 'Speed', 'Generation', 'Legendary']
        expected_columns = set(columns) - \
            set(self.columns_to_keep) | set(new_columns)
        self.assertEqual(expected_columns, set(self.df.columns))

    def test_clean_data(self):
        clean_data(self.df)

        actual_shape = self.df.shape
        expected_shape = (339, 41)

        if (actual_shape[0] == 340):
            self.fail("You avez oublié de drop les doublons")

        if (actual_shape[0] == 804):
            self.fail(
                "Vous avez oublié de drop les lignes avec des valeurs manquantes")

        self.assertEqual(expected_shape, self.df.shape)

        self.assertEqual(list(range(expected_shape[0])), self.df.index.tolist(), "Vous avez oublié de reset l'index")

    # Note: Ce test ne fonctionnera que si vous avez bien implémenté les fonctions précédentes,
    # vu que la modification du type des colonnes se base sur les noms des colonnes renommées
    def test_correct_columns_types(self):
        filter_columns(self.df)
        rename_columns(self.df)
        clean_data(self.df)
        correct_columns_types(self.df)
        self.assertEqual(int, self.df['Generation'].dtype)
        self.assertEqual(int, self.df["HP"].dtype)
        self.assertEqual(int, self.df["Speed"].dtype)


if __name__ == '__main__':
    unittest.main()
