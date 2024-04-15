CREATE TABLE `likes` (
  `id` integer PRIMARY KEY,
  `property_id` integer,
  `user_id` integer,
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `user` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `email` varchar(255),
  `password` varchar(255),
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `property` (
  `id` integer PRIMARY KEY,
  `price` float,
  `city` varchar(255),
  `year` integer,
  `description` varchar(255),
  `created_at` timestamp,
  `updated_at` timestamp
);

ALTER TABLE `likes` ADD FOREIGN KEY (`property_id`) REFERENCES `property` (`id`);

ALTER TABLE `likes` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
