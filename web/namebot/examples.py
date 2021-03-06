from __future__ import absolute_import

from . import nlp
from . import techniques
from . import metrics
from . import scoring
from . import settings as namebot_settings


def example_synsets():
    # TODO: Make class based like metrics
    data = nlp.get_synsets(
        words=namebot_settings.TEST_DATA,
        use_definitions=True)
    return data


def example_synset_categories():
    return nlp.print_all_synset_categories()


def example_techniques():
    # TODO: Make class based like metrics
    return techniques.generate_all_techniques(
        namebot_settings.TEST_DATA)


def example_scoring():
    return scoring.generate_all_scoring(
        namebot_settings.TEST_DATA)


def example_metrics():
    test = metrics.NameBotMetricUtilities()
    allnames = test.open_file(
        '../Research/namebot-fortune-500-companies.html')

    results = {
        'names': allnames,
        'metrics': {}
    }

    results['metrics']['digits_frequency'] = test.get_digits_frequency(allnames)
    results['metrics']['length'] = test.name_length(allnames)
    results['metrics']['vowel_beginning'] = test.name_starts_with_vowel(allnames)
    results['metrics']['vowel_count'] = test.name_vowel_count(allnames)
    results['metrics']['name_length'] = test.name_length(allnames)
    results['metrics']['get_name_spaces'] = test.get_name_spaces(allnames)
    results['metrics']['get_consonant_repeat_frequency'] = test.get_consonant_repeat_frequency(allnames)
    results['metrics']['consonant_duplicate_repeat_frequency'] = test.get_consonant_duplicate_repeat_frequency(allnames)
    results['metrics']['vowel_repeat_frequency'] = test.get_vowel_repeat_frequency(allnames)
    results['metrics']['special_characters'] = test.get_special_chars(allnames)
    results['metrics']['search_results'] = test.get_search_results(allnames)
    results['metrics']['name_numbers'] = test.get_named_numbers(allnames)
    results['metrics']['adj_verb_noun'] = test.get_adjective_verb_or_noun(allnames)
    results['metrics']['get_first_letter_frequency'] = test.get_first_letter_frequency(allnames)
    results['metrics']['get_word_types'] = test.get_word_types(allnames)
    return results


def generate_all_examples():
    example_data = {}
    print '< ##=========##===========##=========## > '
    print '... -=|=- Running ALL the examples -=|=- ... '
    print '< ##=========##===========##=========## > '

    example_data['synsets'] = example_synsets()
    example_data['metrics'] = example_metrics()
    example_data['techniques'] = example_techniques()
    example_data['scoring'] = example_scoring()
    return example_data
