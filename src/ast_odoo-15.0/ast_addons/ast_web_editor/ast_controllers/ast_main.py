Module(
    body=[
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.wrappers', asname=None)],
        ),
        ImportFrom(
            module='PIL',
            names=[
                alias(name='Image', asname=None),
                alias(name='ImageFont', asname=None),
                alias(name='ImageDraw', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='base64',
            names=[
                alias(name='b64decode', asname=None),
                alias(name='b64encode', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[
                alias(name='slug', asname=None),
                alias(name='unslug', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.mimetypes',
            names=[alias(name='guess_mimetype', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.image',
            names=[
                alias(name='image_data_uri', asname=None),
                alias(name='base64_to_image', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.assetsbundle',
            names=[alias(name='AssetsBundle', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='models.ir_attachment',
            names=[
                alias(name='SUPPORTED_IMAGE_EXTENSIONS', asname=None),
                alias(name='SUPPORTED_IMAGE_MIMETYPES', asname=None),
            ],
            level=2,
        ),
        Assign(
            targets=[Name(id='logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_LIBRARY_ENDPOINT', ctx=Store())],
            value=Constant(value='https://media-api.odoo.com', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='Web_Editor',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='export_icon_to_png',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='icon', annotation=None, type_comment=None),
                            arg(arg='color', annotation=None, type_comment=None),
                            arg(arg='bg', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                            arg(arg='alpha', annotation=None, type_comment=None),
                            arg(arg='font', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='#000', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=100, kind=None),
                            Constant(value=255, kind=None),
                            Constant(value='/web/static/lib/fontawesome/fonts/fontawesome-webfont.ttf', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method converts an unicode character to an image (using Font\n            Awesome font by default) and is used only for mass mailing because\n            custom fonts are not supported in mail.\n            :param icon : decimal encoding of unicode character\n            :param color : RGB code of the color\n            :param bg : RGB code of the background color\n            :param size : Pixels in integer\n            :param alpha : transparency of the image from 0 to 255\n            :param font : font path\n\n            :returns PNG image converted from given font\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='size', ctx=Store())],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Constant(value=1, kind=None),
                                    Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Name(id='size', ctx=Load()),
                                            Constant(value=512, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='addons_path', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='addons_manifest',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='web', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='addons_path', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='font_obj', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ImageFont', ctx=Load()),
                                    attr='truetype',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='addons_path', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='font', ctx=Load()),
                                    ),
                                    Name(id='size', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='icon', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='icon', ctx=Load()),
                                        attr='isdigit',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Name(id='chr', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[Name(id='icon', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Name(id='icon', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='bg', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='bg', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='rgba', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='bg', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='bg', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='rgba', kind=None),
                                            Constant(value='rgb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='bg', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Constant(value=',', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='bg', ctx=Load()),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=',', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Constant(value=')', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGBA', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='size', ctx=Load()),
                                            Name(id='size', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='color',
                                        value=Tuple(
                                            elts=[
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draw', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ImageDraw', ctx=Load()),
                                    attr='Draw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='boxw', ctx=Store()),
                                        Name(id='boxh', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='textsize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='icon', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='font',
                                        value=Name(id='font_obj', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='icon', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='font',
                                        value=Name(id='font_obj', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='left', ctx=Store()),
                                        Name(id='top', ctx=Store()),
                                        Name(id='right', ctx=Store()),
                                        Name(id='bottom', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='image', ctx=Load()),
                                    attr='getbbox',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='imagemask', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='L', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='boxw', ctx=Load()),
                                            Name(id='boxh', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='drawmask', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ImageDraw', ctx=Load()),
                                    attr='Draw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='imagemask', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='drawmask', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Name(id='left', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Name(id='top', ctx=Load()),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='icon', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='font',
                                        value=Name(id='font_obj', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fill',
                                        value=Name(id='alpha', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='color', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='rgba', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='color', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='color', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='rgba', kind=None),
                                            Constant(value='rgb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='color', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Constant(value=',', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='color', ctx=Load()),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=',', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Constant(value=')', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='iconimage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGBA', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='boxw', ctx=Load()),
                                            Name(id='boxh', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='color', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='iconimage', ctx=Load()),
                                    attr='putalpha',
                                    ctx=Load(),
                                ),
                                args=[Name(id='imagemask', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='outimage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGBA', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='boxw', ctx=Load()),
                                            Name(id='size', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='bg', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='outimage', ctx=Load()),
                                    attr='paste',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='iconimage', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Name(id='left', ctx=Load()),
                                            Name(id='top', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='iconimage', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='output', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='outimage', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[Name(id='output', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='format',
                                        value=Constant(value='PNG', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='wrappers',
                                        ctx=Load(),
                                    ),
                                    attr='Response',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='mimetype',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='image/png', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='data',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='output', ctx=Load()),
                                    attr='getvalue',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='Cache-Control', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='public, max-age=604800', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='Access-Control-Allow-Origin', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='*', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='Access-Control-Allow-Methods', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='GET, POST', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='Connection', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='close', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='Date', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='strftime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%a, %d-%b-%Y %T GMT', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='gmtime',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='Expires', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='strftime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%a, %d-%b-%Y %T GMT', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='gmtime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='time', ctx=Load()),
                                                        attr='time',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Constant(value=604800, kind=None),
                                                    op=Mult(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/web_editor/font_to_img/<icon>', kind=None),
                                        Constant(value='/web_editor/font_to_img/<icon>/<color>', kind=None),
                                        Constant(value='/web_editor/font_to_img/<icon>/<color>/<int:size>', kind=None),
                                        Constant(value='/web_editor/font_to_img/<icon>/<color>/<int:size>/<int:alpha>', kind=None),
                                        Constant(value='/web_editor/font_to_img/<icon>/<color>/<bg>', kind=None),
                                        Constant(value='/web_editor/font_to_img/<icon>/<color>/<bg>/<int:size>', kind=None),
                                        Constant(value='/web_editor/font_to_img/<icon>/<color>/<bg>/<int:size>/<int:alpha>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update_checklist',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='checklistId', annotation=None, type_comment=None),
                            arg(arg='checked', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='res_model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='filename', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='htmlelem', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='<div>%s</div>', kind=None),
                                        op=Mod(),
                                        right=Name(id='value', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='HTMLParser',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='checked', ctx=Store())],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[Name(id='checked', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='li', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='htmlelem', ctx=Load()),
                                    attr='find',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value=".//li[@id='checklist-id-", kind=None),
                                            op=Add(),
                                            right=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='checklistId', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value="']", kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='li', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_update_checklist_recursive',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='li', ctx=Load()),
                                                Name(id='checked', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='children',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                                keyword(
                                                    arg='ancestors',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='value', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='tostring',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='htmlelem', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='encoding',
                                            value=Constant(value='utf-8', kind=None),
                                        ),
                                        keyword(
                                            arg='method',
                                            value=Constant(value='html', kind=None),
                                        ),
                                    ],
                                ),
                                slice=Slice(
                                    lower=Constant(value=5, kind=None),
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=6, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Name(id='filename', ctx=Load())],
                                        values=[Name(id='value', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='value', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/checklist', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_checklist_recursive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='li', annotation=None, type_comment=None),
                            arg(arg='checked', annotation=None, type_comment=None),
                            arg(arg='children', annotation=None, type_comment=None),
                            arg(arg='ancestors', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='checklist-id-', kind=None),
                                ops=[NotIn()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='li', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='id', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='classname', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='li', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='class', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Compare(
                                    left=Constant(value='o_checked', kind=None),
                                    ops=[In()],
                                    comparators=[Name(id='classname', ctx=Load())],
                                ),
                                ops=[Eq()],
                                comparators=[Name(id='checked', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='checked', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='classname', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s o_checked', kind=None),
                                        op=Mod(),
                                        right=Name(id='classname', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='classname', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\s?o_checked\\s?', kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='classname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='li', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='class', kind=None),
                                    Name(id='classname', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='children', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='node', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='li', ctx=Load()),
                                            attr='getnext',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ul', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='node', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='ul', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ul', ctx=Store())],
                                                    value=Name(id='node', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='tag',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='li', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='node', ctx=Load()),
                                                                        attr='getchildren',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='node', ctx=Load()),
                                                                        attr='getchildren',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='tag',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ul', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ul', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='node', ctx=Load()),
                                                                attr='getchildren',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='ul', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='child', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='ul', ctx=Load()),
                                                    attr='getchildren',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='child', ctx=Load()),
                                                            attr='tag',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='li', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_update_checklist_recursive',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='child', ctx=Load()),
                                                                    Name(id='checked', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='children',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='ancestors', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='allSelected', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ul', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='li', ctx=Load()),
                                            attr='getparent',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='ul', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='li', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ul', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ul', ctx=Load()),
                                                    attr='getparent',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='child', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='ul', ctx=Load()),
                                            attr='getchildren',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='child', ctx=Load()),
                                                            attr='tag',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='li', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='checklist-id', kind=None),
                                                        ops=[In()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='child', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='o_checked', kind=None),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='child', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='class', kind=None),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='allSelected', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='node', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ul', ctx=Load()),
                                            attr='getprevious',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='node', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='node', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ul', ctx=Load()),
                                                            attr='getparent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='getprevious',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='node', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='li', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_update_checklist_recursive',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='node', ctx=Load()),
                                                    Name(id='allSelected', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='ancestors',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='is_image', annotation=None, type_comment=None),
                            arg(arg='quality', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='height', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value='ir.ui.view', kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Name(id='is_image', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='format_error_msg', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value="Uploaded image's format is not supported. Try with: %s", kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=', ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='SUPPORTED_IMAGE_EXTENSIONS', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='data', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='image_process',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='data', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='size',
                                                        value=Tuple(
                                                            elts=[
                                                                Name(id='width', ctx=Load()),
                                                                Name(id='height', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='quality',
                                                        value=Name(id='quality', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='verify_resolution',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mimetype', ctx=Store())],
                                            value=Call(
                                                func=Name(id='guess_mimetype', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='b64decode', ctx=Load()),
                                                        args=[Name(id='data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='mimetype', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='SUPPORTED_IMAGE_MIMETYPES', ctx=Load())],
                                            ),
                                            body=[
                                                Return(
                                                    value=Dict(
                                                        keys=[Constant(value='error', kind=None)],
                                                        values=[Name(id='format_error_msg', ctx=Load())],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='UserError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Dict(
                                                        keys=[Constant(value='error', kind=None)],
                                                        values=[Name(id='format_error_msg', ctx=Load())],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Return(
                                                    value=Dict(
                                                        keys=[Constant(value='error', kind=None)],
                                                        values=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    attr='args',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_clean_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_attachment_create',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Name(id='name', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='data',
                                        value=Name(id='data', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='res_id',
                                        value=Name(id='res_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='res_model',
                                        value=Name(id='res_model', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='_get_media_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/attachment/add_data', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value='ir.ui.view', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_clean_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_attachment_create',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Name(id='url', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='res_id',
                                        value=Name(id='res_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='res_model',
                                        value=Name(id='res_model', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='_get_media_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/attachment/add_url', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='remove',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Removes a web-based image attachment if it is used by no view (template)\n\n        Returns a dict mapping attachments which would not be removed (if any)\n        mapped to the views preventing their removal\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_clean_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Name(id='Attachment', ctx=Store()),
                                Name(id='attachments_to_remove', ctx=Store()),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Views', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.ui.view', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='removal_blocked_by', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='Attachment', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ids', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='html_escape',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='local_url',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='views', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Views', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='|', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='arch_db', kind=None),
                                                            Constant(value='like', kind=None),
                                                            BinOp(
                                                                left=Constant(value='"%s"', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='url', ctx=Load()),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='arch_db', kind=None),
                                                            Constant(value='like', kind=None),
                                                            BinOp(
                                                                left=Constant(value="'%s'", kind=None),
                                                                op=Mod(),
                                                                right=Name(id='url', ctx=Load()),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='views', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='removal_blocked_by', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='views', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Constant(value='name', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='attachments_to_remove', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='attachment', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='attachments_to_remove', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachments_to_remove', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='removal_blocked_by', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/attachment/remove', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_image_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='src', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='This route is used to determine the original of an attachment so that\n        it can be used as a base to modify it again (crop/optimization/filters).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id_match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='^/web/image/([^/?]+)', kind=None),
                                    Name(id='src', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='id_match', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='url_segment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='id_match', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='number_match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='^(\\d+)', kind=None),
                                            Name(id='url_segment', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='.', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='url_segment', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attachment', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.http', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_xmlid_to_obj',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='url_segment', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='number_match', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='attachment', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.attachment', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='number_match', ctx=Load()),
                                                                            attr='group',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value=1, kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='|', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='url', kind=None),
                                                            Constant(value='=like', kind=None),
                                                            Name(id='src', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='url', kind=None),
                                                            Constant(value='=like', kind=None),
                                                            BinOp(
                                                                left=Constant(value='%s?%%', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='src', ctx=Load()),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='mimetype', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='SUPPORTED_IMAGE_MIMETYPES', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='attachment', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='attachment', kind=None),
                                            Constant(value='original', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='attachment', kind=None),
                                    Constant(value='original', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='read',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[Constant(value='id', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='original_id',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='attachment', ctx=Load()),
                                                    ],
                                                ),
                                                attr='read',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='image_src', kind=None),
                                                        Constant(value='mimetype', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/get_image_info', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_attachment_create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value='ir.ui.view', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Create and return a new attachment.', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='name', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='endswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='.bmp', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='name', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=4, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='name', ctx=Load()),
                                    ),
                                    Name(id='url', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='url', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='res_model', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='ir.ui.view', kind=None)],
                                    ),
                                    Name(id='res_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res_id', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='res_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='res_id', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='attachment_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='public', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='res_model', kind=None),
                                ],
                                values=[
                                    Name(id='name', ctx=Load()),
                                    Compare(
                                        left=Name(id='res_model', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ir.ui.view', kind=None)],
                                    ),
                                    Name(id='res_id', ctx=Load()),
                                    Name(id='res_model', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='attachment_data', ctx=Load()),
                                            slice=Constant(value='datas', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='data', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='url', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='attachment_data', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='url', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='url', kind=None),
                                                            Name(id='url', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You need to specify either data or url to create an attachment.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='attachment_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='attachment', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_clean_context',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='allowed_company_ids', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='context', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_assets_editor_resources',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='get_views', annotation=None, type_comment=None),
                            arg(arg='get_scss', annotation=None, type_comment=None),
                            arg(arg='get_js', annotation=None, type_comment=None),
                            arg(arg='bundles', annotation=None, type_comment=None),
                            arg(arg='bundles_restriction', annotation=None, type_comment=None),
                            arg(arg='only_user_custom_files', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            List(elts=[], ctx=Load()),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Transmit the resources the assets editor needs to work.\n\n        Params:\n            key (str): the key of the view the resources are related to\n\n            get_views (bool, default=True):\n                True if the views must be fetched\n\n            get_scss (bool, default=True):\n                True if the style must be fetched\n\n            get_js (bool, default=True):\n                True if the javascript must be fetched\n\n            bundles (bool, default=False):\n                True if the bundles views must be fetched\n\n            bundles_restriction (list, default=[]):\n                Names of the bundles in which to look for scss files\n                (if empty, search in all of them)\n\n            only_user_custom_files (bool, default=True):\n                True if only user custom files must be fetched\n\n        Returns:\n            dict: views, scss, js\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_related_views',
                                    ctx=Load(),
                                ),
                                args=[Name(id='key', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='bundles',
                                        value=Name(id='bundles', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='views', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='views', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='key', kind=None),
                                            Constant(value='xml_id', kind=None),
                                            Constant(value='arch', kind=None),
                                            Constant(value='active', kind=None),
                                            Constant(value='inherit_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='scss_files_data_by_bundle', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='js_files_data_by_bundle', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='get_scss', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='scss_files_data_by_bundle', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_load_resources',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='scss', kind=None),
                                            Name(id='views', ctx=Load()),
                                            Name(id='bundles_restriction', ctx=Load()),
                                            Name(id='only_user_custom_files', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='get_js', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='js_files_data_by_bundle', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_load_resources',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='js', kind=None),
                                            Name(id='views', ctx=Load()),
                                            Name(id='bundles_restriction', ctx=Load()),
                                            Name(id='only_user_custom_files', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='views', kind=None),
                                    Constant(value='scss', kind=None),
                                    Constant(value='js', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='get_views', ctx=Load()),
                                                    Name(id='views', ctx=Load()),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='get_scss', ctx=Load()),
                                                    Name(id='scss_files_data_by_bundle', ctx=Load()),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='get_js', ctx=Load()),
                                                    Name(id='js_files_data_by_bundle', ctx=Load()),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/get_assets_editor_resources', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_load_resources',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='file_type', annotation=None, type_comment=None),
                            arg(arg='views', annotation=None, type_comment=None),
                            arg(arg='bundles_restriction', annotation=None, type_comment=None),
                            arg(arg='only_user_custom_files', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='AssetsUtils', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='web_editor.assets', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='files_data_by_bundle', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resources_type_info', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='t_call_assets_attribute', kind=None),
                                    Constant(value='mimetype', kind=None),
                                ],
                                values=[
                                    Constant(value='t-js', kind=None),
                                    Constant(value='text/javascript', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='file_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='scss', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resources_type_info', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='t_call_assets_attribute', kind=None),
                                            Constant(value='mimetype', kind=None),
                                        ],
                                        values=[
                                            Constant(value='t-css', kind=None),
                                            Constant(value='text/scss', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='excluded_url_matcher', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='compile',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='^(.+/lib/.+)|(.+import_bootstrap.+\\.scss)$', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url_infos', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='v', ctx=Store()),
                            iter=Name(id='views', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='asset_call_node', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='fromstring',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='v', ctx=Load()),
                                                        slice=Constant(value='arch', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//t[@t-call-assets]', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attr', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='asset_call_node', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='resources_type_info', ctx=Load()),
                                                        slice=Constant(value='t_call_assets_attribute', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='attr', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='json', ctx=Load()),
                                                                attr='loads',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='attr', ctx=Load()),
                                                                        attr='lower',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='asset_name', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='asset_call_node', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-call-assets', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='files_data', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='file_info', ctx=Store()),
                                            iter=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.qweb', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get_asset_content',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='asset_name', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='file_info', ctx=Load()),
                                                            slice=Constant(value='atype', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Name(id='resources_type_info', ctx=Load()),
                                                                slice=Constant(value='mimetype', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='url', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='file_info', ctx=Load()),
                                                        slice=Constant(value='url', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='excluded_url_matcher', ctx=Load()),
                                                            attr='match',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='url', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='file_data', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='AssetsUtils', ctx=Load()),
                                                            attr='get_asset_info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='url', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='file_data', ctx=Load()),
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='url_infos', ctx=Load()),
                                                            slice=Name(id='url', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='file_data', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Constant(value='/user_custom_', kind=None),
                                                                ops=[In()],
                                                                comparators=[Name(id='url', ctx=Load())],
                                                            ),
                                                            Subscript(
                                                                value=Name(id='file_data', ctx=Load()),
                                                                slice=Constant(value='customized', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='file_type', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='scss', kind=None)],
                                                                    ),
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Name(id='only_user_custom_files', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='files_data', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='url', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='files_data', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='files_data_by_bundle', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Name(id='asset_name', ctx=Load()),
                                                                    Name(id='files_data', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='files_data_by_bundle', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='bundle_1', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='files_data_by_bundle', ctx=Load()),
                                        slice=Name(id='i', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='j', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='files_data_by_bundle', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='bundle_2', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='files_data_by_bundle', ctx=Load()),
                                                slice=Name(id='j', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='bundle_1', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='bundles_restriction', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='bundle_2', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='bundles_restriction', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='bundle_1', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=ListComp(
                                                        elt=Name(id='item_1', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='item_1', ctx=Store()),
                                                                iter=Subscript(
                                                                    value=Name(id='bundle_1', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Name(id='item_1', ctx=Load()),
                                                                        ops=[In()],
                                                                        comparators=[
                                                                            Subscript(
                                                                                value=Name(id='bundle_2', ctx=Load()),
                                                                                slice=Constant(value=1, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='files_data_by_bundle', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='bundle_1', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='files_data_by_bundle', ctx=Load()),
                                        slice=Name(id='i', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='j', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='i', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='files_data_by_bundle', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='bundle_2', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='files_data_by_bundle', ctx=Load()),
                                                slice=Name(id='j', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='bundle_2', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=ListComp(
                                                elt=Name(id='item_2', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='item_2', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Name(id='bundle_2', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='item_2', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Name(id='bundle_1', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='files_data_by_bundle', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='data', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='data', ctx=Store()),
                                        iter=Name(id='files_data_by_bundle', ctx=Load()),
                                        ifs=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='bundles_restriction', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='bundles_restriction', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='urls', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='bundle_data', ctx=Store()),
                            iter=Name(id='files_data_by_bundle', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='urls', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='bundle_data', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='custom_attachments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='AssetsUtils', ctx=Load()),
                                    attr='get_all_custom_attachments',
                                    ctx=Load(),
                                ),
                                args=[Name(id='urls', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='bundle_data', ctx=Store()),
                            iter=Name(id='files_data_by_bundle', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='bundle_data', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='url', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='bundle_data', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='i', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='url_info', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='url_infos', ctx=Load()),
                                                slice=Name(id='url', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='AssetsUtils', ctx=Load()),
                                                    attr='get_asset_content',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='url', ctx=Load()),
                                                    Name(id='url_info', ctx=Load()),
                                                    Name(id='custom_attachments', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='bundle_data', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='url', kind=None),
                                                    Constant(value='arch', kind=None),
                                                    Constant(value='customized', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='/%s/%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='url_info', ctx=Load()),
                                                                    slice=Constant(value='module', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='url_info', ctx=Load()),
                                                                    slice=Constant(value='resource_path', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='content', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='url_info', ctx=Load()),
                                                        slice=Constant(value='customized', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='files_data_by_bundle', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_asset',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='file_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Save a given modification of a scss/js file.\n\n        Params:\n            url (str):\n                the original url of the scss/js file which has to be modified\n\n            bundle (str):\n                the name of the bundle in which the scss/js file addition can\n                be found\n\n            content (str): the new content of the scss/js file\n\n            file_type (str): 'scss' or 'js'\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='web_editor.assets', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='save_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Name(id='bundle', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                    Name(id='file_type', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/save_asset', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='reset_asset',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        The reset_asset route is in charge of reverting all the changes that\n        were done to a scss/js file.\n\n        Params:\n            url (str):\n                the original URL of the scss/js file to reset\n\n            bundle (str):\n                the name of the bundle in which the scss/js file addition can\n                be found\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='web_editor.assets', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='reset_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Name(id='bundle', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/reset_asset', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='public_render_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='len_args', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='len_args', ctx=Load()),
                                        ops=[GtE()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='len_args', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                ],
                            ),
                            msg=Constant(value='Need a xmlID and potential rendering values to render a template', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='trusted_value_keys', ctx=Store())],
                            value=Tuple(
                                elts=[Constant(value='debug', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xmlid', ctx=Store())],
                            value=Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='len_args', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Subscript(
                                                value=Name(id='args', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='View', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.ui.view', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='View', ctx=Load()),
                                    attr='render_public_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='xmlid', ctx=Load()),
                                    DictComp(
                                        key=Name(id='k', ctx=Load()),
                                        value=Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Name(id='k', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='k', ctx=Store()),
                                                iter=Name(id='values', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='k', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='trusted_value_keys', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/public_render_template', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='modify_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='original_id', annotation=None, type_comment=None),
                            arg(arg='mimetype', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Creates a modified copy of an attachment and returns its image_src to be\n        inserted into the DOM.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='original_id', kind=None),
                                    Constant(value='datas', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='mimetype', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='data', ctx=Load()),
                                    Constant(value='binary', kind=None),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='res_model', ctx=Load()),
                                            Constant(value='ir.ui.view', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='mimetype', ctx=Load()),
                                            Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='mimetype',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='fields', ctx=Load()),
                                    slice=Constant(value='res_model', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ir.ui.view', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='fields', ctx=Load()),
                                            slice=Constant(value='res_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='res_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='fields', ctx=Load()),
                                                    slice=Constant(value='res_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='res_id', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='name', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='fields', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='name', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='attachment', ctx=Load()),
                                attr='url',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='^/\\w+/static/', kind=None),
                                            Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='url',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='url_fragments', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='url_fragments', ctx=Load()),
                                                    attr='insert',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='url',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='/', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='url_fragments', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='attachment', ctx=Load()),
                                attr='public',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='image_src',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='generate_access_token',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s?access_token=%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='image_src',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='access_token',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/modify_image/<model("ir.attachment"):attachment>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_shape_svg',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='segments', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='shape_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Name(id='module', ctx=Load()),
                                    Constant(value='static', kind=None),
                                    Starred(
                                        value=Name(id='segments', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='shape_path', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='exceptions',
                                                ctx=Load(),
                                            ),
                                            attr='NotFound',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='file_open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='shape_path', ctx=Load()),
                                            Constant(value='r', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='filter_ext',
                                                value=Tuple(
                                                    elts=[Constant(value='.svg', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='file', ctx=Store()),
                                ),
                            ],
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='file', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_svg_colors',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='svg', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user_colors', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='svg_options', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_palette', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='1', kind=None),
                                    Constant(value='2', kind=None),
                                    Constant(value='3', kind=None),
                                    Constant(value='4', kind=None),
                                    Constant(value='5', kind=None),
                                ],
                                values=[
                                    Constant(value='#3AADAA', kind=None),
                                    Constant(value='#7C6576', kind=None),
                                    Constant(value='#F6F6F6', kind=None),
                                    Constant(value='#FFFFFF', kind=None),
                                    Constant(value='#383E45', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bundle_css', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='regex_hex', ctx=Store())],
                            value=Constant(value='#[0-9A-F]{6,8}', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='regex_rgba', ctx=Store())],
                            value=Constant(value='rgba?\\(\\d{1,3},\\d{1,3},\\d{1,3}(?:,[0-9.]{1,4})?\\)', kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='colorMatch', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='^c([1-5])$', kind=None),
                                            Name(id='key', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='colorMatch', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='css_color_value', ctx=Store())],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='re', ctx=Load()),
                                                        attr='match',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        BinOp(
                                                            left=Constant(value='(?i)^%s$|^%s$', kind=None),
                                                            op=Mod(),
                                                            right=Tuple(
                                                                elts=[
                                                                    Name(id='regex_hex', ctx=Load()),
                                                                    Name(id='regex_rgba', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='css_color_value', ctx=Load()),
                                                                attr='replace',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value=' ', kind=None),
                                                                Constant(value='', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='match',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='^o-color-([1-5])$', kind=None),
                                                            Name(id='css_color_value', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='bundle_css', ctx=Load()),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='bundle', ctx=Store())],
                                                                    value=Constant(value='web.assets_frontend', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Name(id='files', ctx=Store()),
                                                                                Name(id='_', ctx=Store()),
                                                                            ],
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='request', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='ir.qweb', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_get_asset_content',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='bundle', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='asset', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='AssetsBundle', ctx=Load()),
                                                                        args=[
                                                                            Name(id='bundle', ctx=Load()),
                                                                            Name(id='files', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='bundle_css', ctx=Store())],
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='asset', ctx=Load()),
                                                                                attr='css',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='index_content',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='color_search', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='re', ctx=Load()),
                                                                    attr='search',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='(?i)--%s:\\s+(%s|%s)', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Name(id='css_color_value', ctx=Load()),
                                                                                Name(id='regex_hex', ctx=Load()),
                                                                                Name(id='regex_rgba', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Name(id='bundle_css', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='color_search', ctx=Load()),
                                                            ),
                                                            body=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='werkzeug', ctx=Load()),
                                                                                attr='exceptions',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='BadRequest',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    cause=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='css_color_value', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='color_search', ctx=Load()),
                                                                    attr='group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=1, kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='werkzeug', ctx=Load()),
                                                                        attr='exceptions',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='BadRequest',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='user_colors', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='tools', ctx=Load()),
                                                                    attr='html_escape',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='css_color_value', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='colorMatch', ctx=Load()),
                                                                    attr='group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=1, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='svg_options', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='color_mapping', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='default_palette', ctx=Load()),
                                    slice=Name(id='palette_number', ctx=Load()),
                                    ctx=Load(),
                                ),
                                value=Name(id='color', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='color', ctx=Store()),
                                                Name(id='palette_number', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Name(id='user_colors', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='regex', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='(?i)%s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value='|', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        GeneratorExp(
                                            elt=BinOp(
                                                left=Constant(value='(%s)', kind=None),
                                                op=Mod(),
                                                right=Name(id='color', ctx=Load()),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='color', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='color_mapping', ctx=Load()),
                                                            attr='keys',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='subber',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='match', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='key', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='match', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='key', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='color_mapping', ctx=Load())],
                                        ),
                                        body=Subscript(
                                            value=Name(id='color_mapping', ctx=Load()),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        orelse=Name(id='key', ctx=Load()),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='regex', ctx=Load()),
                                            Name(id='subber', ctx=Load()),
                                            Name(id='svg', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='svg_options', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='shape',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns a color-customized svg (background shape or illustration).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='svg', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='module', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='illustration', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.attachment', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Name(id='unslug', ctx=Load()),
                                                    args=[Name(id='filename', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='binary', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='public',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='url',
                                                            ctx=Load(),
                                                        ),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='httprequest',
                                                                ctx=Load(),
                                                            ),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='exceptions',
                                                        ctx=Load(),
                                                    ),
                                                    attr='NotFound',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='svg', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='b64decode', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='datas',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='svg', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_shape_svg',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='module', ctx=Load()),
                                            Constant(value='shapes', kind=None),
                                            Name(id='filename', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='svg', ctx=Store()),
                                        Name(id='options', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_svg_colors',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='kwargs', ctx=Load()),
                                    Name(id='svg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='flip_value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='flip', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='flip_value', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='x', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='svg', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='svg', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='<svg ', kind=None),
                                            Constant(value='<svg style="transform: scaleX(-1);" ', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='flip_value', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='y', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='svg', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='svg', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='<svg ', kind=None),
                                                    Constant(value='<svg style="transform: scaleY(-1)" ', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='flip_value', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='xy', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='svg', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='svg', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='<svg ', kind=None),
                                                            Constant(value='<svg style="transform: scale(-1)" ', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='svg', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-type', kind=None),
                                                    Constant(value='image/svg+xml', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='Cache-control', kind=None),
                                                    BinOp(
                                                        left=Constant(value='max-age=%s', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='http', ctx=Load()),
                                                            attr='STATIC_CACHE_LONG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/web_editor/shape/<module>/<path:filename>', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='image_shape',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='img_key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='svg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_shape_svg',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='module', ctx=Load()),
                                    Constant(value='image_shapes', kind=None),
                                    Name(id='filename', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='_', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='image_base64', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xmlid',
                                        value=Name(id='img_key', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='model',
                                        value=Constant(value='ir.attachment', kind=None),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Constant(value='datas', kind=None),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='image/png', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='image_base64', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='image_base64', ctx=Store())],
                                    value=Call(
                                        func=Name(id='b64encode', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.http', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_placeholder',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Name(id='base64_to_image', ctx=Load()),
                                args=[Name(id='image_base64', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='width', ctx=Store()),
                                        Name(id='height', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='size', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='size', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='image', ctx=Load()),
                                                    attr='size',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='root', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='svg', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='root', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='width', kind=None),
                                            Constant(value='height', kind=None),
                                        ],
                                        values=[
                                            Name(id='width', ctx=Load()),
                                            Name(id='height', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='svg', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_svg_colors',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='kwargs', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='tostring',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='root', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='pretty_print',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uri', ctx=Store())],
                            value=Call(
                                func=Name(id='image_data_uri', ctx=Load()),
                                args=[Name(id='image_base64', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='svg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='svg', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<image xlink:href="', kind=None),
                                    BinOp(
                                        left=Constant(value='<image xlink:href="%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='uri', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='svg', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-type', kind=None),
                                                    Constant(value='image/svg+xml', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='Cache-control', kind=None),
                                                    BinOp(
                                                        left=Constant(value='max-age=%s', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='http', ctx=Load()),
                                                            attr='STATIC_CACHE_LONG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/web_editor/image_shape/<string:img_key>/<module>/<path:filename>', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='media_library_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='params', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ICP', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ICP', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='web_editor.media_library_endpoint', kind=None),
                                    Name(id='DEFAULT_LIBRARY_ENDPOINT', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='params', ctx=Load()),
                                    slice=Constant(value='dbuuid', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ICP', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='database.uuid', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s/media-library/1/search', kind=None),
                                        op=Mod(),
                                        right=Name(id='endpoint', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Name(id='params', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='status_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='codes',
                                                    ctx=Load(),
                                                ),
                                                attr='ok',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='headers',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='content-type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='application/json', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='status_code',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/web_editor/media_library_search', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_library_media',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='media', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Saves images from the media library as new attachments, making them\n        dynamic SVGs if needed.\n            media = {\n                <media_id>: {\n                    'query': 'space separated search terms',\n                    'is_dynamic_svg': True/False,\n                    'dynamic_colors': maps color names to their color,\n                }, ...\n            }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ICP', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='library_endpoint', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ICP', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='web_editor.media_library_endpoint', kind=None),
                                    Name(id='DEFAULT_LIBRARY_ENDPOINT', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='media_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='media', ctx=Load()),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='dbuuid', kind=None),
                                    Constant(value='media_ids', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ICP', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='database.uuid', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='media_ids', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s/media-library/1/download_urls', kind=None),
                                        op=Mod(),
                                        right=Name(id='library_endpoint', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Name(id='params', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='status_code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='codes',
                                            ctx=Load(),
                                        ),
                                        attr='ok',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="ERROR: couldn't get download urls from media library.", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='id', ctx=Store()),
                                    Name(id='url', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='req', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='_', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='media', ctx=Load()),
                                                            slice=Name(id='id', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='query', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='url', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='/', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='context', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='binary_field_real_user', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.users', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.attachment', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='mimetype', kind=None),
                                                    Constant(value='datas', kind=None),
                                                    Constant(value='public', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='name', ctx=Load()),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='req', ctx=Load()),
                                                            attr='headers',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='content-type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='b64encode', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='req', ctx=Load()),
                                                                attr='content',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=True, kind=None),
                                                    Constant(value='ir.ui.view', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Subscript(
                                        value=Subscript(
                                            value=Name(id='media', ctx=Load()),
                                            slice=Name(id='id', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='is_dynamic_svg', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='colorParams', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='urls',
                                                        ctx=Load(),
                                                    ),
                                                    attr='url_encode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='media', ctx=Load()),
                                                            slice=Name(id='id', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='dynamic_colors', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    slice=Constant(value='url', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='/web_editor/shape/illustration/%s?%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='slug', ctx=Load()),
                                                            args=[Name(id='attachment', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Name(id='colorParams', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachments', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='_get_media_info',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='attachments', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/save_library_media', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_ice_servers',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.ice.server', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_ice_servers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/get_ice_servers', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='bus_broadcast',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='bus_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='res_id', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='check_field_access_rights',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='read', kind=None),
                                    List(
                                        elts=[Name(id='field_name', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='check_access_rule',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='check_field_access_rights',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='write', kind=None),
                                    List(
                                        elts=[Name(id='field_name', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='document', ctx=Load()),
                                    attr='check_access_rule',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Constant(value='editor_collaboration', kind=None),
                                    Name(id='model_name', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='res_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bus_data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='model_name', kind=None),
                                            Constant(value='field_name', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='model_name', ctx=Load()),
                                            Name(id='field_name', ctx=Load()),
                                            Name(id='res_id', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='bus.bus', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sendone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='channel', ctx=Load()),
                                    Constant(value='editor_collaboration', kind=None),
                                    Name(id='bus_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_editor/bus_broadcast', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
