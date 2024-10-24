from owlready2 import *

namespace = 'http://test.org/music.owl'

onto = get_ontology(namespace)


with onto:
    class Music(Thing):
        def tip(self):
            print('Hmm, not sure what your music is..')

    class has_tempo(Music >> int, FunctionalProperty):
        pass

    class has_key(Music >> str, FunctionalProperty):
        pass

    class has_time_signature(Music >> str, FunctionalProperty):
        pass

    class has_lyrics(Music >> bool, FunctionalProperty):
        pass

    class is_instrumental(Music >> bool, FunctionalProperty):
        pass

    class is_popular(Music >> bool, FunctionalProperty):
        pass

    class is_classical(Music >> bool, FunctionalProperty):
        pass

    class has_genre(Music >> str, FunctionalProperty):
        pass

    class SlowAndRelaxing(Music):
        equivalent_to = [
            Music
            & has_tempo.some(ConstrainedDatatype(int, max_inclusive=60))
            & has_genre.value("Ambient")]

        def tip(self): print("It's slow and relaxing! You might want to listen to this while reading or before bed.")

    class FastAndEnergetic(Music):
        equivalent_to = [
            Music
            & has_tempo.some(ConstrainedDatatype(int, min_inclusive=120))
            & has_genre.value("Rock")]

        def tip(self): print("It's fast and energetic! You might want to listen to this while working out or doing chores.")

    class Instrumental(Music):
        equivalent_to = [
            Music
            & is_instrumental.exactly(True)
            & has_genre.value("Classical")]

        def tip(self): print("It's instrumental! You might want to listen to this while studying or working.")

    class WithLyrics(Music):
        equivalent_to = [
            Music
            & has_lyrics.exactly(True)
            & has_genre.value("Pop")]

        def tip(self): print("It has lyrics! You might want to listen to this during a sing-along or karaoke session.")

    class PopularMusic(Music):
        equivalent_to = [
            Music
            & is_popular.exactly(True)
            & has_genre.value("Pop")]

        def tip(self): print("It's popular! You might want to listen to this at a party or social gathering.")

    class ClassicalMusic(Music):
        equivalent_to = [
            Music
            & is_classical.exactly(True)
            & has_genre.value("Classical")]

        def tip(self): print("It's classical! You might want to listen to this for a sophisticated and timeless experience.")


print('Before:')
music1 = Music('music1')
print(music1.name)
music1.tip()

music1.has_tempo = 50
music1.has_genre = "Ambient"

print()

music2 = Music('music2')
print(music2.name)
music2.tip()

music2.has_tempo = 130
music2.has_genre = "Rock"

print()

music3 = Music('music3')
print(music3.name)
music3.tip()

music3.is_instrumental = True
music3.has_genre = "Classical"

print()

music4 = Music('music4')
print(music4.name)
music4.tip()

music4.has_lyrics = True
music4.has_genre = "Pop"

print()

music5 = Music('music5')
print(music5.name)
music5.tip()

music5.is_popular = True
music5.has_genre = "Pop"

print()

music6 = Music('music6')
print(music6.name)
music6.tip()

music6.is_classical = True
music6.has_genre = "Classical"

print()
sync_reasoner()

print('After:')

print(music1.name)
music1.tip()

print()

print(music2.name)
music2.tip()

print()

print(music3.name)
music3.tip()

print()

print(music4.name)
music4.tip()

print()

print(music5.name)
music5.tip()

print()

print(music6.name)
music6.tip()

onto.save(file='music.owl', format="rdfxml")
