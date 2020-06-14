# php-persian-natural-language-processor
simple php and python wrapper on hazm persian text processor.

[![Software License](https://img.shields.io/badge/license-GPL-brightgreen.svg?style=flat-square)](LICENSE)
[![Packagist Version](https://img.shields.io/packagist/v/Mehrdad-Dadkhah/php-persian-natural-language-processor.svg?style=flat-square)](https://packagist.org/packages/Mehrdad-Dadkhah/PersianLanguageProcessor)

## System requirements

* [hazm](https://github.com/sobhe/hazm)

install hazm:

if have not python:

``` sudo apt install python ```

then:

``` sudo apt install python-pip ```

and then:

``` pip install hazm ```


## Installation

```
composer require mehrdad-dadkhah/php-persian-natural-language-processor
```

## Usage

PHP:
```PHP
use MehrdadDadkhah\Language\PersianLanguageProcessor;

$parser = new PersianLanguageProcessor();

$parser->allNLP('سلام. این یک متن تست است. موفق باشید');
```

Python:
```PYTHON
python /path/to/pr/processor.py allNLP json.dumps('سلام. این یک متن تست است. موفق باشید')
```

and the result:

```
array:7 [▼
  "chunksGroup" => array:2 [▼
    "main" => "[سلام NP] . [این یک متن تست NP] [است VP] . [موفق ADJP] [باشید VP]"
    "normalized" => "[سلام NP] . [این یک متن تست NP] [است VP] . [موفق ADJP] [باشید VP]"
  ]
  "postTags" => array:2 [▼
    "main" => array:10 [▶]
    "normalized" => array:10 [▼
      0 => array:2 [▶]
      1 => array:2 [▶]
      2 => array:2 [▶]
      3 => array:2 [▶]
      4 => array:2 [▼
        0 => "متن"
        1 => "N"
      ]
      5 => array:2 [▶]
      6 => array:2 [▶]
      7 => array:2 [▶]
      8 => array:2 [▶]
      9 => array:2 [▶]
    ]
  ]
  "stem" => array:2 [▼
    "main" => array:4 [▶]
    "normalized" => array:4 [▼
      "ADV" => []
      "N" => array:2 [▶]
      "Ne" => []
      "V" => array:3 [▶]
    ]
  ]
  "wordTokenize" => array:2 [▼
    "main" => array:10 [▶]
    "normalized" => array:10 [▼
      0 => "سلام"
      1 => "."
      2 => "این"
      3 => "یک"
      4 => "متن"
      5 => "تست"
      6 => "است"
      7 => "."
      8 => "موفق"
      9 => "باشید"
    ]
  ]
  "lemmatized" => array:2 [▼
    "main" => array:4 [▼
      "ADV" => []
      "N" => array:2 [▼
        0 => "سلام"
        1 => "متن"
      ]
      "Ne" => []
      "V" => array:3 [▼
        0 => "تست"
        1 => "است"
        2 => "بود#باش"
      ]
    ]
    "normalized" => array:4 [▼
      "ADV" => []
      "N" => array:2 [▼
        0 => "سلام"
        1 => "متن"
      ]
      "Ne" => []
      "V" => array:3 [▼
        0 => "تست"
        1 => "است"
        2 => "بود#باش"
      ]
    ]
  ]
  "normalized" => "سلام. این یک متن تست است. موفق باشید"
  "sentTokenize" => array:2 [▼
    "main" => array:3 [▶]
    "normalized" => array:3 [▼
      0 => "سلام."
      1 => "این یک متن تست است."
      2 => "موفق باشید"
    ]
  ]
]
```


----------
## functions
 - normilizeText(string $text)
 - sentTokenizeText(string $text)
 - wordTokenizeText(string $text)
 - postTagText(string $text)
 - chunksText(string $text)
 - getChunksGroup(string $text)
 - stemText(string $text)
 - lemmatizeText(string $text)
 - allNLP(string $text)

allNLP function call all other functions and return all results.

## Acknowledgments

Uses:

* [sobhe/hazm](https://github.com/sobhe/hazm)
* [symfony/process](https://github.com/symfony/Process)

## License

php-persian-natural-language-processor is licensed under the [GPLv3 License](https://opensource.org/licenses/GPL-3.0).
