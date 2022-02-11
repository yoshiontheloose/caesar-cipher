# Cryptography

**Author**: Clarissa
**Version**: 1.0.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for this class. (i.e. What's your problem domain?) -->
Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

Devise a way to decipher the encrypted message event when you do NOT have the key!

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Import Natural Language Toolkit (NLTK) from [Source: nltk.org](https://www.nltk.org/data.html)

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Create an `encrypt` function that takes in a plain text phrase and a numeric shift.

- the phrase will then be `shifted` that many letters.

- shifts that exceed 26 should wrap around.

- shifts that push a letter out or range should wrap around.

Create a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

Create a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

**User Acceptance Tests**:

Encrypt a string with a given shift

Decrypt a previously encrypted string with the same shift.

Encryption should handle upper and lower case letters.

Encryption should allow non-alpha characters but ignore them, including white space.

Decrypt encrypted version of _It was the best of times, it was the worst of times._ WITHOUT knowing the shift used.

## Change Log
<!-- Use this area to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Application now has a fully-functional express server, with a GET route for the location resource. -->

## Estimates
<!-- See below -->
Estimate of time needed to complete: 10 hours

Start time: 2-9-22
Finish time:

Actual time needed to complete:

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->
