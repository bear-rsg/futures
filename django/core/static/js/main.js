
// Bubbles (generate animated circles in background)
// Blank string to append HTML to below
bubbles_html = '';
// Add specified number of bubbles
for (var i = 0; i <= 69; i++){
    // Determine bubble CSS properties using random values
    size = Math.floor(Math.random() * 80) + 10;
    position_top = Math.floor(Math.random() * 100);
    position_left = Math.floor(Math.random() * 100);
    opacity = Math.random() / 2;
    blur = Math.random() / 3;
    if (blur < 0.2) blur += 0.1;
    // Create bubble and add it to bubbles html
    bubbles_html += `<span id="bubble-${i}" style="z-index: 0; width: ${size}px; height: ${size}px; top: ${position_top}vh; left: ${position_left}vw; opacity: ${opacity}; filter: blur(${blur}em);"></span>`;
}
// Inject the bubbles HTML (ignore on create a vision page)
if (!window.location.href.endsWith('/visions/create/')) $('#bubbles').html(bubbles_html);


// Show the permanent/floating create a vision link (ignore on create a vision pages)
if (!window.location.href.includes('/visions/create/')) $('#permanent-vision-create-link').show();
