Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='Command', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='modules', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ImLivechatChannel',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Livechat Channel\n        Define a communication channel, which can be accessed with 'script_external' (script tag to put on\n        external website), 'script_internal' (code to be integrated with odoo website) or via 'web_page' link.\n        It provides rating tools, and access rules for anonymous people.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='im_livechat.channel', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='rating.parent.mixin', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Livechat Channel', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rating_satisfaction_days', ctx=Store())],
                    value=Constant(value=7, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_image',
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
                            targets=[Name(id='image_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='modules', ctx=Load()),
                                    attr='get_module_resource',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='im_livechat', kind=None),
                                    Constant(value='static/src/img', kind=None),
                                    Constant(value='default.png', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='image_path', ctx=Load()),
                                                    Constant(value='rb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='read',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_user_ids',
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
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_uid',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The name of the channel', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='button_text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Text of the Button', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='Have a Question? Chat with us.', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default text displayed on the Livechat Support Button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='default_message', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Welcome Message', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='How may I help you?', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="This is an automated 'welcome' message that your visitor will see when they initiate a new conversation.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='input_placeholder', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Chat Input Placeholder', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Text that prompts the user to initiate the chat.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='header_background_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='#875A7B', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default background color of the channel header once open', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='title_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='#FFFFFF', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default title color of the channel once open', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='button_background_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='#878787', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default background color of the Livechat button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='button_text_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='#FFFFFF', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default text color of the Livechat button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='web_page', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Web Page', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_web_page_link', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='URL to a static page where you client can discuss with the operator of the channel.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='are_you_inside', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Are you inside the matrix?', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_are_you_inside', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='script_external', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Script (external)', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_script_external', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='sanitize',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='nbr_channel', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Number of conversation', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_nbr_channel', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_128', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Image', kind=None)],
                        keywords=[
                            keyword(
                                arg='max_width',
                                value=Constant(value=128, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=128, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_image', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='im_livechat_channel_im_user', kind=None),
                            Constant(value='channel_id', kind=None),
                            Constant(value='user_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Operators', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_user_ids', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='channel_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mail.channel', kind=None),
                            Constant(value='livechat_channel_id', kind=None),
                            Constant(value='Sessions', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rule_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='im_livechat.channel.rule', kind=None),
                            Constant(value='channel_id', kind=None),
                            Constant(value='Rules', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_are_you_inside',
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
                        For(
                            target=Name(id='channel', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='channel', ctx=Load()),
                                            attr='are_you_inside',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uid',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    ListComp(
                                                        elt=Attribute(
                                                            value=Name(id='u', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='u', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='channel', ctx=Load()),
                                                                    attr='user_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_script_external',
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
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='im_livechat.external_loader', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='dbname', kind=None)],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        attr='dbname',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='channel_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='url', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='get_base_url',
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
                                            value=Name(id='record', ctx=Load()),
                                            attr='script_external',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='_render',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='values', ctx=Load())],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_web_page_link',
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='web_page',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Constant(value='%s/im_livechat/support/%i', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='get_base_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_nbr_channel',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='livechat_channel_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='has_message', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='__count', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='livechat_channel_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lazy',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_count', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='x', ctx=Load()),
                                        slice=Constant(value='livechat_channel_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='x', ctx=Load()),
                                    slice=Constant(value='__count', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Name(id='data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='nbr_channel',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_count', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='channel_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_join',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='user_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_uid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_quit',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='user_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=3, kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_uid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_rating',
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
                        Expr(
                            value=Constant(value=" Action to display the rating relative to the channel, so all rating of the\n            sessions of the current channel\n            :returns : the ir.action 'action_view_rating' with the correct context\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.act_window', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='im_livechat.rating_rating_action_livechat', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[Constant(value='search_default_parent_res_name', kind=None)],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_available_users',
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
                        Expr(
                            value=Constant(value=' get available user of a given channel\n            :retuns : return the res.users having their im_status online\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='user', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='im_status',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='online', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_livechat_mail_channel_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='anonymous_name', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='operator_partner_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='operator', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner_to_add', ctx=Store())],
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Command', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='is_pinned', kind=None),
                                                ],
                                                values=[
                                                    Name(id='operator_partner_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='visitor_user', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='user_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='visitor_user', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='user_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='visitor_user', ctx=Load()),
                                            Attribute(
                                                value=Name(id='visitor_user', ctx=Load()),
                                                attr='active',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id='visitor_user', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='operator', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='channel_partner_to_add', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='partner_id', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='visitor_user', ctx=Load()),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
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
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='channel_last_seen_partner_ids', kind=None),
                                    Constant(value='livechat_active', kind=None),
                                    Constant(value='livechat_operator_id', kind=None),
                                    Constant(value='livechat_channel_id', kind=None),
                                    Constant(value='anonymous_name', kind=None),
                                    Constant(value='country_id', kind=None),
                                    Constant(value='channel_type', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='public', kind=None),
                                ],
                                values=[
                                    Name(id='channel_partner_to_add', ctx=Load()),
                                    Constant(value=True, kind=None),
                                    Name(id='operator_partner_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Name(id='user_id', ctx=Load()),
                                        body=Constant(value=False, kind=None),
                                        orelse=Name(id='anonymous_name', ctx=Load()),
                                    ),
                                    Name(id='country_id', ctx=Load()),
                                    Constant(value='livechat', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=' ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    IfExp(
                                                        test=Name(id='visitor_user', ctx=Load()),
                                                        body=Attribute(
                                                            value=Name(id='visitor_user', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Name(id='anonymous_name', ctx=Load()),
                                                    ),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Name(id='operator', ctx=Load()),
                                                            attr='livechat_username',
                                                            ctx=Load(),
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='operator', ctx=Load()),
                                                            attr='livechat_username',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Attribute(
                                                            value=Name(id='operator', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='private', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_open_livechat_mail_channel',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='anonymous_name', annotation=None, type_comment=None),
                            arg(arg='previous_operator_id', annotation=None, type_comment=None),
                            arg(arg='user_id', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Return a mail.channel given a livechat channel. It creates one with a connected operator, or return false otherwise\n            :param anonymous_name : the name of the anonymous person of the channel\n            :param previous_operator_id : partner_id.id of the previous operator that this visitor had in the past\n            :param user_id : the id of the logged in visitor, if any\n            :param country_code : the country of the anonymous person of the channel\n            :type anonymous_name : str\n            :return : channel header\n            :rtype : dict\n\n            If this visitor already had an operator within the last 7 days (information stored with the 'im_livechat_previous_operator_pid' cookie),\n            the system will first try to assign that operator if he's available (to improve user experience).\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='operator', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='previous_operator_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='available_users', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_available_users',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='previous_operator_id', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='available_users', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='partner_id', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='operator', ctx=Store())],
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='available_user', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='available_user', ctx=Store()),
                                                                iter=Name(id='available_users', ctx=Load()),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='available_user', ctx=Load()),
                                                                                attr='partner_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='previous_operator_id', ctx=Load())],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
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
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='operator', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='operator', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_random_operator',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='operator', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mail_channel_vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_livechat_mail_channel_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='anonymous_name', ctx=Load()),
                                    Name(id='operator', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user_id',
                                        value=Name(id='user_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='country_id',
                                        value=Name(id='country_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mail.channel', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_create_nosubscribe',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='mail_channel_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mail_channel', ctx=Load()),
                                    attr='_broadcast',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='operator', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='mail_channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_info',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_random_operator',
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
                        Expr(
                            value=Constant(value=" Return a random operator from the available users of the channel that have the lowest number of active livechats.\n        A livechat is considered 'active' if it has at least one message within the 30 minutes.\n\n        (Some annoying conversions have to be made on the fly because this model holds 'res.users' as available operators\n        and the mail_channel model stores the partner_id of the randomly selected operator)\n\n        :return : user\n        :rtype : res.users\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='operators', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_available_users',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='operators', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="SELECT COUNT(DISTINCT c.id), c.livechat_operator_id\n            FROM mail_channel c\n            LEFT OUTER JOIN mail_message m ON c.id = m.res_id AND m.model = 'mail.channel'\n            WHERE c.channel_type = 'livechat'\n            AND c.livechat_operator_id in %s\n            AND m.create_date > ((now() at time zone 'UTC') - interval '30 minutes')\n            GROUP BY c.livechat_operator_id\n            ORDER BY COUNT(DISTINCT c.id) asc", kind=None),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='operators', ctx=Load()),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='partner_id', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='active_channels', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='dictfetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_channel_operator_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='active_channel', ctx=Load()),
                                    slice=Constant(value='livechat_operator_id', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='active_channel', ctx=Store()),
                                        iter=Name(id='active_channels', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='inactive_operators', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='operator', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='operator', ctx=Store()),
                                        iter=Name(id='operators', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='operator', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[Name(id='active_channel_operator_ids', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='inactive_operators', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='choice',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='inactive_operators', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lowest_number_of_conversations', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='active_channels', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='count', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='less_active_operator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='random', ctx=Load()),
                                    attr='choice',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='active_channel', ctx=Load()),
                                            slice=Constant(value='livechat_operator_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='active_channel', ctx=Store()),
                                                iter=Name(id='active_channels', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='active_channel', ctx=Load()),
                                                            slice=Constant(value='count', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='lowest_number_of_conversations', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='operator', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='operator', ctx=Store()),
                                                iter=Name(id='operators', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='operator', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='less_active_operator', ctx=Load())],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_channel_infos',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='header_background_color', kind=None),
                                    Constant(value='button_background_color', kind=None),
                                    Constant(value='title_color', kind=None),
                                    Constant(value='button_text_color', kind=None),
                                    Constant(value='button_text', kind=None),
                                    Constant(value='input_placeholder', kind=None),
                                    Constant(value='default_message', kind=None),
                                    Constant(value='channel_name', kind=None),
                                    Constant(value='channel_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='header_background_color',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='button_background_color',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='title_color',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='button_text_color',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='button_text',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='input_placeholder',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='default_message',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_livechat_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='username', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='username', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='username', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Visitor', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='info', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='info', ctx=Load()),
                                    slice=Constant(value='available', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_available_users',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='info', ctx=Load()),
                                    slice=Constant(value='server_url', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_base_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='info', ctx=Load()),
                                slice=Constant(value='available', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='options', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_channel_infos',
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
                                            value=Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='options', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='current_partner_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='options', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_username', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='username', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='info', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ImLivechatChannelRule',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Channel Rules\n        Rules defining access to the channel (countries, and url matching). It also provide the 'auto pop'\n        option to open automatically the conversation.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='im_livechat.channel.rule', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Livechat Channel Rules', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence asc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='regex_url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='URL Regex', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Regular expression specifying the web pages this rule will be applied on.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='action', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='display_button', kind=None),
                                            Constant(value='Display the button', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='auto_popup', kind=None),
                                            Constant(value='Auto popup', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='hide_button', kind=None),
                                            Constant(value='Hide the button', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Action', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='display_button', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="* 'Display the button' displays the chat button on the pages.\n* 'Auto popup' displays the button and automatically open the conversation pane.\n* 'Hide the button' hides the chat button on the pages.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auto_popup_timer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Auto popup timer', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Delay (in seconds) to automatically open the conversation window. Note: the selected action must be 'Auto popup' otherwise this parameter will not be taken into account.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='channel_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='im_livechat.channel', kind=None),
                            Constant(value='Channel', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The channel of the rule', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.country', kind=None),
                            Constant(value='im_livechat_channel_country_rel', kind=None),
                            Constant(value='channel_id', kind=None),
                            Constant(value='country_id', kind=None),
                            Constant(value='Country', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="The rule will only be applied for these countries. Example: if you select 'Belgium' and 'United States' and that you set the action to 'Hide Button', the chat button will be hidden on the specified URL from the visitors located in these 2 countries. This feature requires GeoIP installed on your server.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Matching order', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Given the order to find a matching rule. If 2 rules are matching for the given url/country, the one with the lowest sequence will be chosen.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='match_rule',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='channel_id', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' determine if a rule of the given channel matches with the given url\n            :param channel_id : the identifier of the channel_id\n            :param url : the url to match with a rule\n            :param country_id : the identifier of the country\n            :returns the rule that matches the given condition. False otherwise.\n            :rtype : im_livechat.channel.rule\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_match',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='rules', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='rule', ctx=Store()),
                                    iter=Name(id='rules', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='rule', ctx=Load()),
                                                                attr='regex_url',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='url', ctx=Load()),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=Name(id='rule', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='country_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='country_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[Name(id='country_id', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='channel_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='channel_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='rule', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_match', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='rule', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Name(id='rule', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='country_ids', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='channel_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='channel_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='_match', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
