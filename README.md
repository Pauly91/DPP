# DPP

The goal of this project is to use the SmartNoise sdk in a MITM proxy that sits between a querier and a database.

* The user should be able to make basic aggregate queries as permitted
in SmartNoise such as count() and sum() but should reject other queries.
* The interface itself should use a simple config file which defines what queries are allowed and what the parameters should be for the interface.

Refer to this link for the tech-specs: [Link](https://docs.google.com/document/d/1Up2pG3Q17O37CDpZ5BMFxB0581DOfUUZDPI2Dqm_I_g/edit?usp=sharing)