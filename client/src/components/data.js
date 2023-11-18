export const categories = [
  {
    id: 1,
    name: 'Käekellad',
    showSublist: false,
    sublist: [
      { id: 11, name: 'Mehaanilised' },
      { id: 12, name: 'Kvartskellad' },
      { id: 13, name: 'Hübriidilised' },
    ],
  },
  {
    id: 2,
    name: 'Printerid',
    showSublist: false,
    sublist: [
      { id: 21, name: 'Laserprinterid' },
      { id: 22, name: 'Tindiprinterid' },
      { id: 23, name: '3D-printerid' },
    ],
  },
  {
    id: 3,
    name: 'Kõrvaklapid',
    showSublist: false,
    sublist: [
      { id: 31, name: 'Kõrvapealsed' },
      { id: 32, name: 'Sisemised' },
    ],
  },
  { id: 4, name: 'Arvutid', showSublist: false, sublist: [
      { id: 41, name: 'Sülearvutid' },
      { id: 42, name: 'Tahvelarvutid' },
      { id: 43, name: 'Lauaarvutid' },
    ]
  },
  { id: 5, name: 'Telefonid', showSublist: false, sublist: [
      { id: 51, name: 'Nutitelefonid' },
      { id: 52, name: 'Nuputelefonid' },
      { id: 53, name: 'Lauatelefonid' },
    ]
  },
];

export const products = [
  {
    title: 'Käekellad',
    description: 'Siin on mingi kirjeldus nendele ägedatele käekelladele',
    price: '14 EUR/kuus',
    date: new Date('2023-11-20'),
  },
  {
    title: 'Teine toode',
    description: 'Teise toote kirjeldus',
    price: '19 EUR/kuus',
    date: new Date('2023-12-15'),
  },
  {
    title: 'Kolmas toode',
    description: 'Kolmanda toote kirjeldus',
    price: '121 EUR/kuus',
    date: new Date('2023-12-14'),
  },
];
