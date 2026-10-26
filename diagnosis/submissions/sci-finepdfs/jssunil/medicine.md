# Medicine sheet: sci-finepdfs (jssunil)

Written from the first 150 rows of the pack (500 in all), as the Tue 27 Oct checkpoint. Diseases found more than five
times so far: **C2**.

Status: DRAFT. The 150 labelled rows were filled from an automatic script and are marked `read=partial` (not yet read
in full by a person). The counts below come from those labels. The gold-set harm test has not been run because the gold
set was not available when this was written.

## Medicine 1: C2 repeated lines

1. **Disease:** C2, in 46 of the first 150 documents (a line of 4 or more characters repeated 5 or more times in one
   document). Three examples:
   - `8c1aed2f8a439b91` (row 0): the line `MIT Introduction to Deep Learning` repeated 8 times, first at offset 56 (slide-deck footer).
   - `73fbd40e1111121e` (row 10): the line `DRAWING NOS. AR 14-2019` repeated 48 times (page header on every page).
   - `507d7cf0978d22e4` (row 4): the line `Health Resources and Services Administration` repeated 5 times.

2. **Medicine:** in words: inside one document, keep the first copy of any line of 20 or more characters that
   occurs 5 or more times, and remove the later copies. Lines made only of table characters (`|`, `-`, `:`,
   spaces) are never removed, so markdown tables stay intact.

   ```python
   import re
   from collections import Counter

   SEPARATOR = re.compile(r"^[\s|:\-]+$")

   def remove_repeated_lines(text, min_len=20, min_repeats=5):
       lines = text.split("\n")
       counts = Counter(l.strip() for l in lines)
       seen, kept = set(), []
       for line in lines:
           s = line.strip()
           if len(s) >= min_len and counts[s] >= min_repeats and not SEPARATOR.match(s):
               if s in seen:
                   continue
               seen.add(s)
           kept.append(line)
       return "\n".join(kept)
   ```

3. **Action:** fix the text (remove the repeated copies). Do not drop the document.

4. **Harm test:** NOT RUN on the gold set (the gold set for this pack was not available). Measured on the 150
   labelled rows only, as a first estimate and not a replacement for the harm test:
   - the rule changes 38 of the 46 documents labelled C2 (the other 8 only repeat table separator lines or short
     lines, which the rule keeps) and removes 97,076 of the 9,193,251 characters in those 46 documents (1.1%);
   - over all 150 rows it changes 38 documents (25%) and removes 97,076 of 12,054,761 characters (0.81%);
   - it changes 0 of the 103 rows labelled `clean`. This is a weak check: those rows were filled from the script and
     not read by a person, so they are not yet a reliable proxy gold set.

   The fraction of the gold set that it changes or drops must be measured and must be 1% or less. To fill in once the
   gold set is available:
   - gold documents changed: ___
   - gold documents dropped: 0 (the rule never drops)

5. **Side effects:** the cases where the medicine is wrong:
   - Repeated lines that are real content, for example a repeated equation in `776e2d329eaeeb77`
     (`\end{cases} \Rightarrow \begin{cases}`, 5 times) or the same table row in a spreadsheet-like page.
   - Slide decks where each slide ends with the same footer: removing later copies is correct, but the first copy
     is kept in the middle of the text.
   - Legal or form text where a short repeated clause (for example a refrain) is meant to repeat.
   - Lines of 20 or more characters that repeat 5 or more times by chance in very long documents (200,000+
     characters): the thresholds should scale with the document length. This is still to be tested.

No other disease reached more than five documents in the first 150 rows (B2 1, A6 1), so no other section is written.
F1 (personal data) is not auto-detected for phone numbers, so its count is not known yet.
