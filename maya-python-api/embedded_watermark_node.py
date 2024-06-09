from PySide2 import QtCore
from PySide2 import QtGui

import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr  # pylint: disable=E0001,E0611
import maya.api.OpenMayaUI as omui

import maya.cmds as cmds


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


class WatermarkNode(omui.MPxLocatorNode):

    TYPE_NAME = "watermarknode"
    TYPE_ID = om.MTypeId(0x0007F7FA)
    DRAW_CLASSIFICATION = "drawdb/geometry/watermark"
    DRAW_REGISTRANT_ID = "WatermarkNode"


    def __init__(self):
        super(WatermarkNode, self).__init__()

    @classmethod
    def creator(cls):
        return WatermarkNode()

    @classmethod
    def initialize(cls):
        pass


class WatermarkDrawOverride(omr.MPxDrawOverride):

    NAME = "WatermarkDrawOverride"


    def __init__(self, obj):
        super(WatermarkDrawOverride, self).__init__(obj, None)

        self.image_hex_str = "89504e470d0a1a0a0000000d49484452000000a00000002108060000005e23a050000000097048597300000b1300000b1301009a9c180000176549444154789ced7c6b8c655775e6f7adbdcfb9b7aa5f74b7ddc66d9bf6db8003768c49420027c84c1e04628684280f82348c321ae5479891469a1ff36b7ecccf3c50446646493442831c920c8f60c0980026f1808d12131b70086a63bbdbed36ddb86df7abeadeb3f75edffcd8e7dcbad55d75ab8902fe31bda472dfba75ce3e6bafbd9edf5ac794848b74915e2ab2979a818bf4ff375d54c08bf492d24505bc482f295d54c08bf492525cf4c7eddb5bb81c4d1cb5a3d1f665c9cb05ae2b49b1e414059d70974a11ccd82e8dc74b168c67ce9c99acae4e2666d5060461d48e6066180a234988218e969697c625274c56565720a5540aa62901008c8c7bf6eedd6666eeee08663873f614722ad3a66d3a77552b932003ba694208013136f0b9e7b46dbbdcb66d0ba9d088d3a7cf38e153d272e58ec85d824b9084a66dd1360de64b3892a3f178b4e4ae021040c6e933a7bd09cd2a09afdf112967a4d481044843086d95800033d8b6a5e5eda16990532a67cf9e5d01ea6308c2e5483921982136016606a321950c3861e44e065c6de4cb695c96632af7ef893c0ce078ea12dad10874472e1926e16ccf19008c6255094268620040b80a4442d9413208381023af10f0320060c68b808e16e3613325c9e0a520360d9433b03a01009cf2f30bde850a386c5ac27e2fe53a5759bd400504c0b1a417249d800452007055f17295e001c09110ecdb330514aa14a441de2041c16fc839ed752f24f1b86847288759155930db593cbf566ec9e5921b49c08c67253d0be0d886dc11a086cf04a4eb4ac9fb20add28d460ae04900df057062fdbd8497028f01c63983810e945cae7079071064a1d1bcbfff5900a7b61036086c772fb7aa10eede017804c064fed91b5265618711b780f64a002f973006d0913c01f252498f823cba90872d88c00d34de22f100801d0020c369024f03d80ee01b00fc42d75ba880218cea4915bf633a5979e3ecc42e80821926d3f4915c8a9a18509d8b7eb69b4e6e2105a33d366a4707e79925aaf2cd89b885fbaf4f5757f6820042b857c29136b6585a5a020048ba264d27bf86418151bd4ad304493a05e2945c0f03f802800e204a7184e0b030539ea694f48e52ba03c383cd0ca46509a7499e48d9ef03f0f5e1ef396734318011184e1fc2dba793959bd6364034a181a004e024aa127e09c037d55b9c9961341a41f27e03baa24bd3df40d701848f46a367011caafb2272cee852b74ed6927605b3b78760af8278e9600e33f74cee27f01a33dea9180f03ba07c093177c9895de18a2fd346097036ad6fd85d827f03a03eea0f8ac802ff7fbdc32622e54403280046458a2bc2ae3c65762d8ad04846070d71329e707dd85a6993da6ab4188704135eaac29f506cb3b800ee4e01c4b7d9ac118fa055c0421aedd3ffb87dc0569578876953b5e25cf7f0ce0b42414af0ad893aa171c6e1e186124b15bd0ee26866be9fae434a57bc9aa385dcabda2cef8adbc0ebff7eb116c245d02e01292af26f99910ec5312400ed161b688860548d8b91eef5ce583f4e32184774ada33b8d041f9aa639ff100493b82f166923788f89caa226e45bb48fe2669afa991acca67f0fac3337a3e4dd21546fc0acc6e05f42100cf2d5a7ca10276dd149210823d19ccf67835d37544b0004a00af04b0930648c839978f99d92404d65ca932dc273e0084246ce95105603a770819a8399bbbf70a58a5c2e17ada11b9af0abe4cd8a524475e0fe32633fbb740f90000a52e23980d5e5000d29ae6f04540cfb8fb3692fb21b430583b6ade59e447ddcba37513e789639ed7b3209f71b911d841f23289903c3431bca3894bcfe5921e920a72ee1042dbcb48ce992221694ee63967945240022ec1683f1b637897b4a66d128e8b7c82f26773d1846434c33e4957d3ec402fbf96c6b7c71877a9cb776fb4912a4c5d4ada6f13b6bfd732489e00fe138023ee7e4a822cd84e4857027825c95612ccec4680ef97f44113bebbd9012f54c0c964da27e8cde76c34be5ff2bcee021a097929694708f1bfb0b7fe9cfd6b25e7834683d99ab5fc336933b77b1e495a4d297d20c478da73b71443dc2fd91dc1f8135e85f2aa18c39b243c0054abdd8837f7f21532fc55ca29c410af8931fc92bb5feb24da36bebdebd2a3035be738a8b5e02bfebd8377e792118cbb5c767d1bc35d022f830009ef04f418a0d317240412936e02f71aaadb36fc58139b77b97c485a26903e5172f90786f822ad5a3949c81df2d2b8dbeb9b10de49729724c4d8bc3909534cd35f823cd71dbcccc8df117c5f159101f27fc8595f00cac1a669d6f15652020cd71be3dbcc78732fd77d16e2ef785bfe9ba4b31bed6b210c53ad99837b4da81e49448d1b653af1e96405a4fd8c99ed06000967bb2e7d42bd9b0e315c887cff458824524a25a50ec16c95e077ba9cfe5797f3d76b750dc4185e6714820dc50ecf5b8364ee3f17108f17953f9334e955ee32b2b9928c2017daafd82b00c9935ef4f0ca64fa4140abaa517637116e8022a0ad6d4c02daa641db44b46ddc376adbf7a84f60289d2839ff8188fb49beb8897052c9fe9554ca07241d3333b8fba1021e1cb2efc6ac4f758410c23b40eeab95b981e83e954bfa1f240e6e54089104c1c7734e1f74e5bfadd53991bdfcdd4af1bcb241050c5c40157cde830038044f1d4a4a0881fb638c3fe32e98115dca0f15d709b31a1637adda7e304492cb25e5950cc328126d7dfc83ee7a6dbd44bb42cc7dd21a364b0222e0330fa9ace366f63ca4fd005b07f71138b2052f2382880c70396880b28e15f7a76208af92049a5d5ac3ed62199144ca1d24078d68627c0381515dd75452ba9be49346aecbfad7a5b5a87920c5674af13f07f006521f85ca0b00104d88a140ca20ed1566f127245425cae9abf2ee1eb3165b05330225e57437a225b9be935279d8cbe645f1052b606ffd48a5432a5ddd4c4bb4edf85fafa5203a9d52fe74ff191a2ab11fa20e0e7977ce8045009130311143d58968510140ce4958545b3571269e4652eb7dd540727a015b12a0be5802c882180d5085546a71c0c602870261e1ae5c05c91302c36e886fae4517514af9aa4bdf2480d21f74357a21e70250689a00b8c00aeb01c063921e230103617d0e3de08c31861f2311fbc2fc744ef9afc266818caad828adfa5133c89324ff0bf595266b35b5e1ed17a8808420b8e70ac25a33548bb7c1ecb572470801abab938f9552ce0e9e63d4363361fcb0c85d2480d1b885050ef0c6f5405534779e593d133300340d077cf2bc6586eb537140b83606db4302729df25c9e1a0a0585b0d0816515d00889984e52dcb6adb9dabd1e4a4ef9642e054dd3a069c20225140c860843603860663b5cd54377297d6e8643968c86114647ce09a538622448830884883e89aac0ba3b1042405b8402816608e09231dc3c54cfb994af9bd989ba590c8512bcc7d5d99b3c69954f026003c040030288260404db38dbdb1a882620394a29b5336171a8622d46fb45b9606628253fd175f92b43655b93dcb00605fc70c847a3e6246beb03842130de5254de32bbc0fd50e8e1176ee09a2555ef6e848460e0eb40fcb20423a994f21773ce6787820b68ce5ba3a755502845884640b0f1b87d8f197743d5a4dd75d80ba00b7003a4c12c8266370c184b297e58d23a6039ab80c9eb3eceb58c355c70f62b67c5870014c0ec329297f7f7bb4b5f63088008870056f968939c0e0002db1afd58a30801c8370ec30bb7be349e17ae1003671600f22d002e67ef1d73299fae16512d61b30af3074912628ce116402f94a2dd907e54d4ad2463af30a54bf9ff0280bb301a19c25ceb6f201aef0070b3a4ed242e411fd552ca9f2c2af78dc62d4a2af0d9219fbf4f519781b8ce0c26e9caa6096f2479550f512097fc55b01c0e11d8aa7120013443443090fb8716228d4f8cdb76ddc3a7d3daa2fc7ee59f9223064308b8447d592d29c58023bddbacbc00d01645d33cbcb6150f8bcbb8b99b05af7a57b3856d31da9d0040034af16f7449df8c7dce24096d1311c2a2b0f22f4f2446247f4b423516a0efafd60ca74be9c3928e0cde61b30249d24e923be70fb12a0eaf8a8c3f29e9c1fe2b945210c286e1e54720fc480c368b008206cffabd52f429b202e0665b200504e00e7787994506434507757aab0206c0ab09dcc6cdbb12ad05fb7628e1a1b61dc3c826a7821ecf3ddd255f5d87ab9335975da39d00df0621a03ee35c602a4278d18127003c76eec31703d17dc37f6db11ad646edf85f01dcdbb394bb2edd33ffd45901f25290d62c15409ffcea7097d2bdeefadac05fdb360b31cab5efd73a1b246f8b66b7a59caf1570b7249f7609db96c7e77b51ccd2adb9ef98e5fa3a80bf24f07c8f4df620f4e65e907da781c61e0c1e5c14799e333ae77712d71af1e64d0b41094d085db3d43c544aaeb9200d7def24a4ecb32cb90e8718466d33bfaf6d00deb2599e4f12057e42ae29be5f053cd743d450c07d21f0addee77e29e70773f1436684f7794108f643f77e3d8713806749ee1dbc5ccae55329779f8b214c078f16e322ef4c48fe1080070010f0e0d2ee60f1a7015cedee68627c73b2fc782ee5a1055ef404c816b50b02492f745dfad36076b062a395bf3a09b345ef9e801c43dff2ac0d051074c90524d8de97b83d6398293130432f8ee49c90528710ec6ced4d0b20b68f9bb813e064b87983d0bee66be64431f3fa35a77e3e043ebf11738b157003b31935cd5d121b427069653a4df7001502a802358c47a3d9c3cf5b72f8c0b9c4e23c9aff7aae4c258756e486e4c299c964f207cbcbe3f71a79a300d07065764c2587505b58d16a2fd737488cfba2e92880c7073f263826d3f4480cf6ef630cafac1e34be85d023666152abdaf93588e2faa217ff46db86ffea2e92dc0e7097e702b88322888010e20519aa4bc8c515020e058b3fea7210b89ea1182bc83293dd50654b824bffe82eb9ab0f67ecdc7d7734be15442b512eadd409a20080c70024928da4c68cd742383e130e805c7ae5adff3905f02f08444805301198887a13816bebe490af78d18600f91603a95cf71342b8318478bb541bf925977b4bf193001043c0d2b8c5d2b85acf30ed718e8e0da37990c4a10550c38f00ab964db3e147b46a2435923ae5be698827b82ce17b39978f83744188166eddb634fe1533822ec00115df50f9e668bcf6517d08c46a29e53e00dee7835748da399d4ed1a5b40ee7520d6b7b72c9c7a65dfa9bdedb36a336becfccaed63039416cc5c78cdc2bae578a3f39d8a4c4bd347ba5300c44104d1311fa9cb25ffb2909f74af83cc0cf7729ff6d97d2df831ccc795a727e5a15ff4308f6bcbb0e579913005fb7da254c52c234650c1daee1645d5811f00581f749f8bcbb7fa1cbf9cbeefea2f54881a0efbafcf846fb5aa880c600b3d0e704c6a6697f7900164bf167734e5f0a468c472d9697c7eb8649d74e63960d01d019f6002ac95d5dea9a943af4e9f9acbab2d820d49f2061e7200c2ff954ea26f052362c204898917b2793ee89ae4b9f351a5c4230de69166e156ab726a5829c375ee31ce62110b48051db60346a4e48ea9379360e348ef361265566b6051a2693eea3a59463a4c1a1604df82d04ee901132a29473f2ec05bc54af86c3deb7d248b164fb859403540c9e2b5c331eb568db0643bf7638137787978226c69f22d1d4affdb0bb1f777794e248a92477ffc6e0412dd84d3186eb9a18d6a69a2498d5e2ae8e6556084712a6932924bfa609e135a2202195a2875d1bf7bc172a60f6829c3344a069c29b481c18608494d227620cddf2f2183186cd2d99846bf07a388ade82ccec15ee7e79ca795691b217964ac674da21e77c3bc09df57b20171dce8e39f8638353924812eefe19494ff7878651d3fc26697d6eb8c5514b9af14443080d7271e4e22f27660d600dd34155e1e6b60cc0dd7dd4b600d04dbaee7f9bc159fbea9798d9bbe68b9cad48129ad820c600412b25fb17e7767cbd19de366f032e470c01e3f108cdec6cea156ddbdcda36f10e778106a454ee070623122c10c5cb5724bdd0cb78346adbf736316e9f1babeb91b8be8b224128b55f3d6ac7a3187f0d640311eefea4bb1fda0c0d5ea880ee8e5243dea869c39d83154ea6d307413e321e8fb6c49baae71256563b4cbbfc8f90a6bda2c5f178e9dde3f178e9bc702a87bbef2b39fd2259117ab80e97e247ddb530ef166a61e85ed2743afd10fb112e40db97c6a3df689a480b01a514b8fb868aecaee9da9eaae548da0ee817344b1bf45c1bc399a5718b711b6705d81c239080e5f118721ccc39fff5ac8235fe64d384d75b0830034a99825c0cc58410ea82eec8393f504a79d2fae18140dc45e0ad983bcf210d0a611de87c4b08e17dee4e3343c97a3ce7f2880b58635f70d7c95ccafd6136b0ab97937c9f5cbb36973b40605b3b6afe0d831de865ab94f22725df5447161621664308b39f82eb72007590943c1e43b8d65d3bb4b9f6598fd21faf0c0aeefe4271ff74db36efcab920186f20c3fb5de593a823dd5300cb2ebca26dc2afbafb6e00406d39dd4bf764fd216c46b5dd369c55793aa5fcf1d1a87d772e0516ece6e0e1e7b3a7cf2c403d40f21500ae47cd05c7122e8d21bc01d065e8fbbb936efa4097cbe9a6e64de72b20aa6f1b8a9dd549fac4d292bdda6660347f55c25380be575b9c8b8787356b7715482a39978f8610fe030363ed4af0dd206e24f96548cf00388bea0c5b027b00be3e04bb53d230e49a26d3e9478abbcf8c700ed3994ebafb02784368c26bfa1ef3cd20ff1381bf01f02d01275927a402801d06bbc682fd9c7bb99ca8455ecef9d3ee7e70d1beb618c90f30f79d6d137f6e6da0416a63bc0bc05d65c194431fa6ef2f451f09c110cd904bc1b44b9f9770f5a88db7e5e220708dd1de2fd73320ce90d80d699ffa35cc0c5d973e9b73f91a4104637dd96563bdefd3affe83882ee5fb19ecb54d08371577c418de26f963ee3a241744cdeeabbb13620cb703b87d68cb0d185dcd5f038acab7dcfd01a046897578fd1c2f43be1c43407679c9e5c371d4fee7528a49da6ee07bc1f0bbc90bdca7086109523977631af86a9a06a5e461ef07bdf81f99d9bf0331ee61a75b48de22e014c9130232c86d21d8fe618dfe1d9cd5d5d5c97f2fc59fde2c0f2689d5e9f44fc618fd766ce24da51440da67c677d38203380a6905406b66fb482ed78cb962afc5fd4baead27ae17cf0382cb4d13df4360db9c6c6dadcadd92aca6656b3f3997d2a5fcc7ee7a80e44c5b485c01f84d24f761c82daae7fb6ccef9e335d43b428c188fc7183a086616e6785b926052c5cd5c402e5e2693ee43824ef6c26ec6a3f63fc660fb07b88235feb5c322ebf65743664d030014f7078aeb7f825821eb8c1efaaa90f5a59c4178239288666862452852ce4f4da7d38f85a13b42dce8caef03aa62f705dfbc5368cc2c0e86184240db8ee6e5fb98e7fc7b723d5d8b923ec4933b055c03e90690fbab5654c570f77f5a5d5dfddd52fcdb17302a37599d747fd875ddfd31541efa506e24af84742380ab492ed7c336803699e6fc7fdcfdcfb6ce6eb7f4803c10821d70d751f0c2df74022ac0ae7e147b40d05deadb49f4e2fab0a0c708bc89e44d201bcd86a93075f9a3dd247dd1812783198ae7da0f35435a5d7b394fc41991c7fb56d38a19d29cee0c8772a2ebf2479b26febc242fc23ed06e97ca3d5e5c009ce45112db00ccbff94798b9173f06f913a07dcb5d4769bdd1a01a81af19e33320f600882e3f06014ea278190a134c3bff6b0be1f260e126772fa0bd3ac6d1d5ee78aaeb2690b01a0cc750d1e9494a69658e9bf5f0130190874a29bfeff25b41de61e41592a206d44e728726707c9be0c3a594474bf18edc00b138876a31879472f908c94724bc2104bb59d23600869a834a5206f1dd92f3c39394fe2e86f05c8817866f72d1454be3764f88cdb2848a957c1f64a495944e955256878ab2eb13ffb66d306a5b142f80b0ecaeeb43e0be088cb2342da53c63d1be93a6a563a893b5259799a799efcf8610da381eef412f88d44d5e40df5af0de0b9a11b1896862bcc45d46b3885242c9f99922b924c4a67959086149d2dc6b07646c422ea93b03cf1d4333782ea42e81562754e644b383e4363363cae97429f9cc5085abcf5d45a26dda518c618fbb0ac9250867bbae7b2ee504336bc6e3f11e92907b1634dbcfb0e7923342e86111af2f58094271df6d215c15c8bd8db0e48067e28c508ec9f974b438911cd3ae03c079c319ce6cbd72f4f9746c6c684a34345e65c0e5466e0f4248c4d4e5cf9bf190173d3f9976188d5ac450abef94d6c4d9a5f56f74005b28e045ba483f68baf8bfe6b8482f295d54c08bf492d2ff0393795309c2f23bd20000000049454e44ae426082"
        self.texture = None

        self.update_texture_by_hex_str()

    def __del__(self):
        self.release_texture()

    def release_texture(self):
        if self.texture:
            texture_manager = omr.MRenderer.getTextureManager()
            texture_manager.releaseTexture(self.texture)
            self.texture = None

    def update_texture_by_hex_str(self):
        if self.image_hex_str:
            qimage = QtGui.QImage()

            ba = QtCore.QByteArray(bytearray.fromhex(self.image_hex_str))
            buffer = QtCore.QBuffer(ba)
            if buffer.open(QtCore.QIODevice.ReadOnly):
                qimage.load(buffer, "PNG")
                qimage = qimage.convertToFormat(QtGui.QImage.Format_RGBA8888)
            else:
                om.MGlobal.displayError("Failed to load image data")
                return

            texture_manager = omr.MRenderer.getTextureManager()

            texture_desc = omr.MTextureDescription()
            texture_desc.setToDefault2DTexture()
            texture_desc.fWidth = qimage.width()
            texture_desc.fHeight = qimage.height()

            image_bytes = qimage.constBits().tobytes()

            self.texture = texture_manager.acquireTexture("", texture_desc, image_bytes, False)

            if not self.texture:
                om.MGlobal.displayError("Unsupported image data")

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        self.vp_width = frame_context.getViewportDimensions()[2]

        if self.texture:
            texture_desc = self.texture.textureDescription()
            self.half_width = 0.5 * texture_desc.fWidth
            self.half_height = 0.5 * texture_desc.fHeight

    def supportedDrawAPIs(self):
        return (omr.MRenderer.kAllDevices)

    def hasUIDrawables(self):
        return True

    def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
        draw_manager.beginDrawable()

        if self.texture:
            draw_manager.setTexture(self.texture)
            draw_manager.setTextureSampler(omr.MSamplerState.kMinMagMipLinear, omr.MSamplerState.kTexClamp)
            draw_manager.setTextureMask(omr.MBlendState.kRGBAChannels)
            draw_manager.setColor(om.MColor((1.0, 1.0, 1.0, 1.0)))

            rect_center = om.MPoint(self.vp_width - (50 + self.half_width), 50 + self.half_height)
            draw_manager.rect2d(rect_center, om.MVector(0.0, 1.0, 0.0), self.half_width, self.half_height, True)

        draw_manager.endDrawable()

    @classmethod
    def creator(cls, obj):
        return WatermarkDrawOverride(obj)


def initializePlugin(plugin):

    vendor = "Chris Zurbrigg"
    version = "1.0.0"
    api_version = "Any"

    plugin_fn = om.MFnPlugin(plugin, vendor, version, api_version)

    try:
        plugin_fn.registerNode(WatermarkNode.TYPE_NAME,              # name of the node
                               WatermarkNode.TYPE_ID,                # unique id that identifies node
                               WatermarkNode.creator,                # function/method that returns new instance of class
                               WatermarkNode.initialize,             # function/method that will initialize all attributes of node
                               om.MPxNode.kLocatorNode,              # type of node to be registered
                               WatermarkNode.DRAW_CLASSIFICATION)    # draw-specific classification string (VP2.0)
    except:
        om.MGlobal.displayError("Failed to register node: {0}".format(WatermarkNode.TYPE_NAME))

    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(WatermarkNode.DRAW_CLASSIFICATION,     # draw-specific classification
                                                      WatermarkNode.DRAW_REGISTRANT_ID,      # unique name to identify registration
                                                      WatermarkDrawOverride.creator)         # function/method that returns new instance of class
    except:
        om.MGlobal.displayError("Failed to register draw override: {0}".format(WatermarkDrawOverride.NAME))


def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)
    try:
        omr.MDrawRegistry.deregisterDrawOverrideCreator(WatermarkNode.DRAW_CLASSIFICATION, WatermarkNode.DRAW_REGISTRANT_ID)
    except:
        om.MGlobal.displayError("Failed to deregister draw override: {0}".format(WatermarkDrawOverride.NAME))

    try:
        plugin_fn.deregisterNode(WatermarkNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Failed to unregister node: {0}".format(WatermarkNode.TYPE_NAME))


if __name__ == "__main__":

    cmds.file(new=True, force=True)

    plugin_name = "embedded_watermark_node.py"

    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

    cmds.evalDeferred('cmds.createNode("watermarknode")')

