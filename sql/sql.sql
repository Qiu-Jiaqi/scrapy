CREATE TABLE `allgame` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `download` (
  `top` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `new` (
  `top` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `reserve` (
  `top` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `sell` (
  `top` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `played` (
  `top` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `amway` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `recommend` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `sole` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `alone` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `rpg` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `action` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `moba` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `strategy` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `card` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `survival` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `simulation` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `racing` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `puzzle` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `quadratic` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `category` varchar(100) NOT NULL,
  `install_num` int(11) NOT NULL,
  `follow_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);
