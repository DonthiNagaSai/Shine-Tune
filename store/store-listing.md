# Play Store listing

Copy for the Google Play Console entry, plus the answers the forms expect.
Everything here describes the app **as it stands today**: no ads, no analytics,
no network use. Revisit all of it if AdMob is added.

---

## App details

| Field | Value |
| --- | --- |
| App name (30 char max) | `Shine & Tune` (12) |
| Application ID | `com.donthinagasai.shinetune` |
| Category | Games → Simulation |
| Tags | Tycoon, Idle, Casual |
| Contact email | *(your public support address — it appears on the store page)* |
| Privacy policy URL | `https://donthinagasai.github.io/Shine-Tune/privacy.html` once Pages is on |

---

## Short description

80 characters maximum. Shown under the title in search results.

```
Wash, fix and serve across six busy plazas. Build your own service empire.
```

(73 characters.)

Alternatives if you want to A/B them later:

```
One washer, one empty lot. Grow it into the busiest plaza in town.
```
```
Serve customers, buy shops, hire staff. A plaza tycoon you can play offline.
```

---

## Full description

4000 characters maximum. Plain text; Play renders limited formatting.

```
One washer. One empty lot. Build the busiest plaza in town.

You start with a single washing machine and a patch of empty paving. Customers
walk in with laundry, you carry it to the washer, hand it back clean, and pocket
the coins. Spend those coins on a second washer. Then a car wash. Then a pet
salon, a phone repair kiosk, a fuel station, a drive-in cinema.

Before long you are running a plaza so busy you cannot keep up — which is when
you start hiring the staff who take the work off your hands.

ELEVEN SHOPS TO BUILD
Laundromat, car wash, fuel station, car repair, drive-in theatre, pet salon,
pet clinic, pet playhouse, phone repair, juice bar and snack bar. Each one grows
from one station to four, and each has its own speed and price upgrades.

SIX PLAZAS, EACH WITH ITS OWN MIX
Corner Lot, Fuel Row, Drive-In Field, Pet Street, Market Street and the Grand
Plaza, where all eleven shops run side by side. Every plaza is a fresh start
with bigger numbers and a different puzzle.

SHOPS THAT DEPEND ON EACH OTHER
This is not eleven separate games on one screen. The car wash and the pet salon
burn a clean towel per customer and drop the dirty one in a bin — and those
towels go back through the same washers your laundry customers are queueing for.
Every wash, bath and juice draws from one shared water tank. Parts, fuel, fruit
and medicine arrive at depots at the edge of the plaza and have to be carried in.
Build too fast in one place and something else runs dry.

RUN IT YOURSELF, THEN AUTOMATE IT
Early on you do every job: carry the laundry, work the counter, send cars through
the tunnel, chase the dog that bolted off the grooming table. Hire a cashier, a
groomer, a towel runner, a supply runner, and watch the plaza start running
without you.

PLAYS ANYWHERE
No internet needed. No account. Nothing to sign up for. One hand, portrait,
pick it up for two minutes or an hour.

Available in English, Spanish, Portuguese, Hindi, Telugu, Indonesian and Arabic.
```

---

## Graphics checklist

| Asset | Size | Status |
| --- | --- | --- |
| App icon | 512 × 512 PNG | done — `app/resources/icon.png`, resized |
| Feature graphic | 1024 × 500 PNG | to do |
| Phone screenshots | 2–8, min 320px, 16:9 or 9:16 | to do |
| Promo video | YouTube link | optional |

Screenshots worth taking, in this order: the Grand Plaza at full tilt, the
drive-in with cars parked at the screen, the laundromat with six washers running,
a shop mid-purchase with the coins flying, and the plaza select screen.

---

## Data safety form

The app sends nothing off the device, so the form is short.

| Question | Answer |
| --- | --- |
| Does your app collect or share any of the required user data types? | **No** |
| Is all of the user data collected by your app encrypted in transit? | n/a — no data collected |
| Do you provide a way for users to request that their data is deleted? | n/a — no data collected |

Note in the form that game progress is stored locally on the device and is removed
when the app is uninstalled. Local-only storage is not "collection" under Google's
definition, which covers data transmitted off the device.

**If you add AdMob, this changes.** Advertising ID becomes collected and shared,
and the form has to be refiled before that release.

---

## Content rating questionnaire

Expected answers, all "no": violence, blood, sexual content, profanity,
controlled substances, gambling, user-generated content, user-to-user
communication, location sharing, personal information sharing.

The only "yes": the app is a game, category Simulation. Expected outcome is
everyone / PEGI 3 / IARC equivalent.

---

## Target audience and ads

| Question | Answer |
| --- | --- |
| Target age groups | **13+** |
| Appeals to children? | No |
| Contains ads? | **No** (today) |

Choosing 13+ keeps the app out of Google's Families policy, which imposes much
stricter ad and content rules. The cartoon art and the pets make the "appeals to
children" question worth answering carefully — if you later market it at younger
players you must move to the Families programme.

---

## Before you submit

- [ ] Fill the contact email and developer name into `privacy.html`
- [ ] Turn on GitHub Pages so the privacy URL resolves
- [ ] Confirm `Shine & Tune` is not already taken on the store
- [ ] Decide whether v1 ships all six plazas or three
