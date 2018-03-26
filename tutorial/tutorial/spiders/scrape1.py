import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
   
    def start_requests(self):
        urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://www.mgm.com/',
        'http://www.focusfeatures.com/films',
'http://www.focusfeatures.com/possession',
'http://www.focusfeatures.com/far_from_heaven',
'http://www.focusfeatures.com/the_pianist',
'http://www.focusfeatures.com/deliver_us_from_eva',
'http://www.focusfeatures.com/the_shape_of_things',
'http://www.focusfeatures.com/swimming_pool',
'http://www.focusfeatures.com/lost_in_translation',
'http://www.focusfeatures.com/sylvia',
'http://www.focusfeatures.com/long_time_dead',
'http://www.focusfeatures.com/21_grams',
'http://www.focusfeatures.com/eternal_sunshine_of_the_spotless_mind',
'http://www.focusfeatures.com/ned_kelly',
'http://www.focusfeatures.com/my_little_eye',
'http://www.focusfeatures.com/the_door_in_the_floor',
'http://www.focusfeatures.com/vanity_fair',
'http://www.focusfeatures.com/the_motorcycle_diaries',
'http://www.focusfeatures.com/rory_oshea_was_here',
'http://www.focusfeatures.com/brothers',
'http://www.focusfeatures.com/my_summer_of_love',
'http://www.focusfeatures.com/broken_flowers',
'http://www.focusfeatures.com/the_constant_gardener',
'http://www.focusfeatures.com/pride_and_prejudice',
'http://www.focusfeatures.com/the_ice_harvest',
'http://www.focusfeatures.com/brokeback_mountain',
'http://www.focusfeatures.com/something_new',
'http://www.focusfeatures.com/brick',
'http://www.focusfeatures.com/on_a_clear_day',
'http://www.focusfeatures.com/scoop',
'http://www.focusfeatures.com/hollywoodland',
'http://www.focusfeatures.com/the_ground_truth',
'http://www.focusfeatures.com/catch_a_fire',
'http://www.focusfeatures.com/the_secret_life_of_words',
'http://www.focusfeatures.com/evening',
'http://www.focusfeatures.com/talk_to_me',
'http://www.focusfeatures.com/eastern_promises',
'http://www.focusfeatures.com/lust,_caution',
'http://www.focusfeatures.com/reservation_road',
'http://www.focusfeatures.com/dan_in_real_life',
'http://www.focusfeatures.com/atonement',
'http://www.focusfeatures.com/in_bruges',
'http://www.focusfeatures.com/the_other_boleyn_girl',
'http://www.focusfeatures.com/miss_pettigrew_lives_for_a_day',
'http://www.focusfeatures.com/hamlet_2',
'http://www.focusfeatures.com/burn_after_reading',
'http://www.focusfeatures.com/milk',
'http://www.focusfeatures.com/coraline',
'http://www.focusfeatures.com/sin_nombre',
'http://www.focusfeatures.com/the_limits_of_control',
'http://www.focusfeatures.com/away_we_go',
'http://www.focusfeatures.com/thirst',
'http://www.focusfeatures.com/taking_woodstock',
'http://www.focusfeatures.com/9',
'http://www.focusfeatures.com/a_serious_man',
'http://www.focusfeatures.com/pirate_radio',
'http://www.focusfeatures.com/greenberg',
'http://www.focusfeatures.com/babies',
'http://www.focusfeatures.com/the_kids_are_all_right',
'http://www.focusfeatures.com/the_american',
'http://www.focusfeatures.com/its_kind_of_a_funny_story',
'http://www.focusfeatures.com/somewhere',
'http://www.focusfeatures.com/the_eagle',
'http://www.focusfeatures.com/jane_eyre',
'http://www.focusfeatures.com/hanna',
'http://www.focusfeatures.com/beginners',
'http://www.focusfeatures.com/one_day',
'http://www.focusfeatures.com/the_debt',
'http://www.focusfeatures.com/tinker_tailor_soldier_spy',
'http://www.focusfeatures.com/pariah',
'http://www.focusfeatures.com/being_flynn',
'http://www.focusfeatures.com/seeking_a_friend_for_the_end_of_the_world',
'http://www.focusfeatures.com/moonrise_kingdom',
'http://www.focusfeatures.com/paranorman',
'http://www.focusfeatures.com/for_a_good_time,_call...',
'http://www.focusfeatures.com/anna_karenina',
'http://www.focusfeatures.com/hyde_park_on_hudson',
'http://www.focusfeatures.com/promised_land',
'http://www.focusfeatures.com/admission',
'http://www.focusfeatures.com/the_place_beyond_the_pines',
'http://www.focusfeatures.com/the_worlds_end',
'http://www.focusfeatures.com/closed_circuit',
'http://www.focusfeatures.com/dallas_buyers_club',
'http://www.focusfeatures.com/that_awkward_moment',
'http://www.focusfeatures.com/bad_words',
'http://www.focusfeatures.com/the_signal',
'http://www.focusfeatures.com/wish_i_was_here',
'http://www.focusfeatures.com/the_boxtrolls',
'http://www.focusfeatures.com/kill_the_messenger',
'http://www.focusfeatures.com/the_theory_of_everything',
'http://www.focusfeatures.com/mr._turner',
'http://www.focusfeatures.com/black_sea',
'http://www.focusfeatures.com/fifty_shades_of_grey',
'http://www.focusfeatures.com/insidious:_chapter_3',
'http://www.focusfeatures.com/self/less',
'http://www.focusfeatures.com/sinister_2',
'http://www.focusfeatures.com/suffragette',
'http://www.focusfeatures.com/the_danish_girl',
'http://www.focusfeatures.com/race',
'http://www.focusfeatures.com/london_has_fallen',
'http://www.focusfeatures.com/the_young_messiah',
'http://www.focusfeatures.com/kubo_and_the_two_strings',
'http://www.focusfeatures.com/american_honey',
'http://www.focusfeatures.com/loving',
'http://www.focusfeatures.com/nocturnal_animals',
'http://www.focusfeatures.com/a_monster_calls',
'http://www.focusfeatures.com/the_zookeepers_wife',
'http://www.focusfeatures.com/the_book_of_henry',
'http://www.focusfeatures.com/the_beguiled',
'http://www.focusfeatures.com/atomic_blonde',
'http://www.focusfeatures.com/victoria_&_abdul',
'http://www.focusfeatures.com/darkest_hour',
'http://www.focusfeatures.com/lady_bird',
'http://www.focusfeatures.com/phantom_thread',
'http://www.focusfeatures.com/thoroughbreds',
'http://www.focusfeatures.com/film_title',
'http://www.focusfeatures.com/walk_of_shame',
'http://www.focusfeatures.com/i_am_ali',
'http://www.focusfeatures.com/maps_to_the_stars',
'http://www.focusfeatures.com/5_flights_up',
'http://www.focusfeatures.com/a_little_chaos',
'http://www.focusfeatures.com/cop_car',
'http://www.focusfeatures.com/trash',
'http://www.focusfeatures.com/mr._right',
'http://www.focusfeatures.com/term_life',
'http://www.focusfeatures.com/search_party',
'http://www.focusfeatures.com/puerto_ricans_in_paris',
'http://www.focusfeatures.com/a_tale_of_love_and_darkness',
'http://www.focusfeatures.com/kicks',
'http://www.focusfeatures.com/in_a_valley_of_violence',
'http://www.focusfeatures.com/raw',
'http://www.focusfeatures.com/film_title',
'http://www.focusfeatures.com/tully',
'http://www.focusfeatures.com/pope_francis:_a_man_of_his_word',
'http://www.focusfeatures.com/won’t_you_be_my_neighbor?',
'http://www.focusfeatures.com/captive_state',
'http://www.focusfeatures.com/the_little_stranger',
'http://www.focusfeatures.com/boy_erased',
'http://www.focusfeatures.com/mary_queen_of_scots',
'http://www.focusfeatures.com/on_the_basis_of_sex',
'http://www.focusfeatures.com/black_klansman',
'http://www.focusfeatures.com/mustang',
'http://www.focusfeatures.com/reflective_light',

        ]
        for url in urls:
            yield scrapy.Request(url=url.lower(), callback=self.parse)
   

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
