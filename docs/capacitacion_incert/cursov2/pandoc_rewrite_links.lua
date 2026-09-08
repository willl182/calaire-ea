local targets = {}

for line in string.gmatch(os.getenv("CALAIRE_LINK_TARGETS") or "", "[^\n]+") do
  local path, article_id, heading_prefix = line:match("^([^\t]+)\t([^\t]+)\t([^\t]+)$")
  if path then
    targets[path] = { article_id = article_id, heading_prefix = heading_prefix }
  end
end

function Link(link)
  local path, fragment = link.target:match("^([^#]+)(#.*)$")
  if not path then
    path = link.target
  end

  local target = targets[path]
  if not target then
    return nil
  end

  if fragment then
    link.target = "#" .. target.heading_prefix .. fragment:sub(2)
  else
    link.target = "#" .. target.article_id
  end
  return link
end
