merge :: (Ord a) => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x <= y    = x : merge xs (y : ys)
    | otherwise = y : merge (x : xs) ys

mergeSort :: (Ord a) => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = let (ys, zs) = halve xs in merge (mergeSort ys) (mergeSort zs)
               where halve xs = splitAt (length xs `div` 2) xs

--halve :: [a] -> ([a], [a])
--halve xs = splitAt (length xs `div` 2) xs
