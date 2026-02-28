
-- Летающие символы на экране (GLua)
-- Путь для сохранения: garrysmod/lua/autorun/client/floating_symbol.lua




local symbol = "卐" -- Символ
local fontName = "FloatingSymbolFontLarge"
local symbolCount = 20 -- Количество символов на экране



-- Создаем крупный шрифт
surface.CreateFont(fontName, {
    font = "Arial",
    size = 250,
    weight = 800,
})

local symbols = {}

-- Инициализация символов
local function InitSymbols()
    symbols = {}
    for i = 1, symbolCount do
        table.insert(symbols, {
            x = math.random(0, ScrW() - 100),
            y = math.random(0, ScrH() - 100),
            vx = math.random(-200, 200),
            vy = math.random(-200, 200),
            col = Color(255, 0, 0)
        })
    end
end

InitSymbols()

hook.Add("HUDPaint", "FloatingSymbolExample", function()
    local frameTime = FrameTime()
    local sw, sh = ScrW(), ScrH()
    
    surface.SetFont(fontName)
    local tw, th = surface.GetTextSize(symbol)

    for _, s in ipairs(symbols) do
        -- Обновляем позицию
        s.x = s.x + s.vx * frameTime
        s.y = s.y + s.vy * frameTime
        
        -- Отскок от краев
        if s.x + tw > sw or s.x < 0 then
            s.vx = -s.vx
            s.x = math.Clamp(s.x, 0, sw - tw)
        end
        
        if s.y + th > sh or s.y < 0 then
            s.vy = -s.vy
            s.y = math.Clamp(s.y, 0, sh - th)
        end
        
        -- Отрисовка
        draw.SimpleText(symbol, fontName, s.x, s.y, s.col)
    end
end)

-- Переинициализация при смене разрешения
hook.Add("OnScreenSizeChanged", "ResetFloatingSymbols", function()
    InitSymbols()
end)

