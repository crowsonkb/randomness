randomness
==========

Generates random secrets (passwords, etc).

Installation
------------

.. code-block:: bash

  python3 setup.py install

Usage
-----

.. code-block:: bash

  # Generates eight-character alphanumeric passwords
  randomness

  # Generates five-word passphrases based on the EFF's short word list
  randomness --set eff4 --length 5 --sep ' '

References
----------

Word list sources:

- `Diceware <http://world.std.com/~reinhold/diceware.html>`_
- `EFF word lists <https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases>`_
