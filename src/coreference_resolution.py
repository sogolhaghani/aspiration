import spacy
import neuralcoref

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 10300000 # or even higher

# # # Add neural coref to SpaCy's pipe

neuralcoref.add_to_pipe(nlp)

# # You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
text = u'''Each edition of a textbook must be as vital, dynamic, and responsive to change as the ﬁeld it covers.
To remain an effective teaching instrument, it must reﬂect the development of the ﬁeld and continue to challenge its readers.
We have seen the focus of personality study shift from global theories, beginning with Sigmund Freud’s 19th-century psychoanalytic theory of neuroses, to 21st-century explorations of more limited personality dimensions.
And we have seen the basis of personality exploration change from case studies of emotionally disturbed persons to more scientiﬁcally based research with diverse populations.
Contemporary work in the ﬁeld reﬂects differences in gender, age, and sexual orientation as well as ethnic, racial, religious, and cultural heritage.
New and Expanded Coverage Major changes for this edition include new biographical material for the theorists, to suggest, where warranted, how the development of their theory may have been inﬂuenced by events in their personal and professional lives.
This approach shows students that the development of science through theory and research is not always totally objective.
It may also derive from intuition and personal experience later reﬁned and extended by more rational, analytic processes.
Social and cultural inﬂuences on the theorists’ beliefs about human nature are described.
The sections on personality research have been updated with more than 300 new references to maintain the emphasis on current issues.
Considerable material has been added on the effects of gender, ethnicity, and culture on the issues of personality development, test performance, and the broader conceptions of human nature.
We present the results of cross-cultural research and a diversity of samples of research participants from more than 45 nations throughout the world, not only English-speaking countries but also countries in Europe, Asia, the Middle East, Africa, and South America.
We have expanded coverage of ethnic issues in personality assessment among African American, Asian American, Hispanic American, and Native American populations.
There is new material on personality assessment including computerized test taking and the use of personal electronic devices as diaries for recording samples of thoughts and behaviors.
We describe the increasing use of the Internet as a psychology laboratory to sample a greater number and variety of subjects online.
For Freudian theory, we have added more than two dozen new studies on concepts such as the inﬂuence of the unconscious, ego control, ego resiliency, displaced aggression, repressors and non-repressors, and dream content.
For Jung, we discuss research on the development of the Myers-Briggs Type Indicator and on behavioral differences as a function of psychological type.
We have added research on the midlife crisis in women, a stage of life Jung considered to be particularly important.
And we include more description of Jung’s psychotherapy sessions with his patients.
For Adler, we present new ﬁndings on early memories, birth order and social interest.
For Horney, we have expanded the coverage of neurotic competitiveness.
For the chapter on Murray there is additional material on the needs for achievement and afﬁliation.
For Erikson there is extensive biographical material from a new book by his daughter.
In addition, we offer more coverage of psychosocial stages of identity, ethnic identity, gender preference identity, cultural differences in the search for identity, and the role of the Internet in creating a virtual identity.
As the general population ages, we have more research available on the issues of generativity in middle age and ego integrity in old age.
For Allport, we discuss more research on expressive behavior, computer recognition of facial expressions and emotions, and the computer transmission of facial expressions through the use of “emoticons.”
To reinforce ﬁndings on the genetic basis of personality, we present new research growing out of Eysenck’s work and the ﬁve-factor model.
The Maslow chapter contains additional work on self-esteem, and the Skinner chapter includes research with human subjects on superstitious behavior and on self-control.
The Bandura chapter contains more material on self-efﬁcacy, on the relationship between video games and aggressive behavior, and on the effect of rap music on aggressive behavior.
The Rotter chapter has new biographical material and updated research on locus of control.
The chapter on limited-domain approaches, or the study of speciﬁc facets of personality, evaluates new forms of sensation seeking, such as tattooing, body piercing, and Internet addiction.
Cultural differences in optimism/pessimism are reported as well as cross-cultural research on positive psychology and the different types of Organization of the Text
The ninth edition of Theories of Personality retains its orientation toward undergraduate students who have had little previous exposure to personality theories.
Our purpose is to reach out to beginning students and ease their task of learning about the study of personality.
We have chosen theorists who represent psychoanalytic, neopsychoanalytic, life-span, trait, humanistic, cognitive, behavioral, and social-learning approaches, as well as clinical and experimental work.
The concluding chapter reviews the seven major perspectives from which to view personality development and suggests ways to help students draw conclusions and achieve closure from their studies.
Each theory in the text is discussed as a unit.'''
sample = u'My sister has a dog. She loves him'
doc = nlp(text)

doc._.has_coref
print(doc._.coref_resolved)
# print(doc._.coref_clusters[1].mentions[-1]._.coref_cluster.main)

# token = doc[-1]
# token._.in_coref
# print(token._.coref_clusters)


# span = doc[-1:]
# print(span)
# span._.is_coref
# span._.coref_cluster.main
# span._.coref_cluster.main._.coref_cluster
# print(span._.coref_cluster.main._.coref_cluster)

# print(doc._.coref_clusters[1].mentions[-1].start)